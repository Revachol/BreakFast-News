from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import aiohttp
import asyncio
from datetime import datetime, timedelta
from TfidfVectorizer.TfidfVectorizer import calculate_tfidf
import requests


def parce_lenta_ru(soup, target_url, title, mongo):
    if "news" not in target_url:
        return

    article = {"title": title, "link": target_url, "key_words": []}

    news_items = soup.find_all(["p"])  # Выбор элементов, содержащих текст новостей
    document = ""  # составляем только первые 30 слов
    counter = 60
    for item in news_items:
        text = item.get_text(strip=True)
        if text:  # Если текст не пустой
            document += text
            counter -= 1
        if counter == 0:
            break
            # print("НОВОСТЬ - ПАРСИМ ТЕГИ")
    # записываем в монгу
    mongo.insert_one(
        {
            "link": target_url,
            "text": document,
        }
    )

    article["key_words"] = calculate_tfidf(document, mongo)

    # отправляю article на бекенд
    url = "http://127.0.0.1:8000/article"  # Добавлено 'http://'

    response = requests.post(url, json=article)

    if response.status_code == 200:
        print("Данные успешно отправлены!")
    else:
        print("Ошибка при отправке данных:", response.status_code, response.text)


parcer_func = {"lenta.ru": parce_lenta_ru, "mash.ru": parce_lenta_ru}


class Crawler:
    def __init__(self, sites, max_depth, collection):
        self.sites = sites
        self.max_depth = max_depth
        self.cache = {}
        self.mongo = collection

    async def parse_website(self, session, target_url, max_depth, current_depth=0):
        if current_depth > max_depth:
            return  # Прекращаем, если достигли максимальной глубины

        # Проверяем кэш
        if target_url in self.cache and self.cache[target_url]:
            return  # Если сайт уже был парсирован, выходим из рекурсии

        try:
            async with session.get(target_url) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, "html.parser")

                    # Сохраняем результат в кэш как True
                    self.cache[target_url] = True  # Кэшируем, что сайт был парсирован
                    print(
                        f"{'  ' * current_depth} {current_depth} Parsed {target_url}: {soup.title.text}"
                    )  # Выводим информацию о текущем парсинге

                    domain = urlparse(target_url).netloc

                    # запускаем кастомный парсер считающий метрику для новости
                    # делаем только, если в монге еще нет такоего target url
                    existing_document = self.mongo.find_one({"link": target_url})
                    if not existing_document:
                        parcer_func[domain](
                            soup, target_url, soup.title.text, self.mongo
                        )

                    # Извлечение всех ссылок на странице
                    links = [
                        urljoin(target_url, a["href"])
                        for a in soup.find_all("a", href=True)
                    ]
                    for link in links:
                        # Проверяем, что ссылка ведет на тот же домен
                        if urlparse(link).netloc == urlparse(target_url).netloc:
                            await self.parse_website(
                                session, link, max_depth, current_depth + 1
                            )  # Рекурсивный вызов
                else:
                    print(f"Ошибка при парсинге сайта {target_url}: {response.status}")
        except Exception as e:
            print(f"Ошибка при запросе к {target_url}: {e}")

    async def get_last_parse_time(self, session, api_url):
        """
        запрашиваем, для которых нужно обновить инфу
        """
        return datetime.now() - timedelta(hours=2)

    async def process_site(self, session, site, max_depth):
        last_parse_time = await self.get_last_parse_time(session, site["target_url"])
        if last_parse_time is not None:
            current_time = datetime.now()
            if current_time - last_parse_time > timedelta(hours=1):
                await self.parse_website(session, site["target_url"], max_depth)
                # Обновляем время последнего парсинга (если нужно)
                # await session.post(site['api_url'], json={'last_parse_time': current_time.isoformat()})

    async def run(self):
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [
                    self.process_site(session, site, self.max_depth)
                    for site in self.sites
                ]
                await asyncio.gather(*tasks)
                await asyncio.sleep(300)  # Ожидание 5 минут перед следующей проверкой
