import time

import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        time.sleep(1)

    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    # print(scrape_novidades(fetch("https://blog.betrybe.com/")))
    selector = Selector(html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page

    # print(scrape_next_page_link(fetch("https://blog.betrybe.com/page/76")))
    # Já é retornado None se não houver o seletor


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
