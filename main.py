import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
from crawler.crawler import Crawler
from pymongo import MongoClient

# Пример данных для 100 сайтов
SITES = [
    # {
    #    "target_url": "https://lenta.ru/",
    # },
    # {
    #    "target_url": "https://mash.ru/news/",
    # },
    {"target_url": "https://journal.tinkoff.ru/tag/breaking-news/"},
]

client = MongoClient("mongodb://root:example@localhost:27017/")
db = client["articles_db"]  # Название базы данных
collection = db["articles_collections"]

if __name__ == "__main__":

    crawler = Crawler(
        SITES, max_depth=2, collection=collection
    )  # Установите необходимую глубину здесь
    asyncio.run(crawler.run())
