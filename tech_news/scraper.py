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
    selector = Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    c_count = selector.css(".post-comments h5::text").re_first(r"\d+") or 0
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    tags = selector.css("a[rel=tag]::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": c_count,
        "summary": ''.join(summary).strip(),
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
