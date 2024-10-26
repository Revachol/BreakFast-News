import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from crawler.crawler import Crawler

# Пример данных для 100 сайтов
SITES = [
    {
        "api_url": "https://example.com/api/site1",
        "target_url": "https://lenta.ru/news/2024/10/26/v-kurskoy-oblasti-vpervye-za-30-let-poyavilsya-novyy-naselennyy-punkt/",
        # "target_url": "https://lenta.ru/news/",
    },
]


if __name__ == "__main__":

    crawler = Crawler(SITES, max_depth=2)  # Установите необходимую глубину здесь
    asyncio.run(crawler.run())
