from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
    data_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news['title'], news['url']) for news in data_list]


# Requisito 7
def search_by_date(date):
    try:
        date_to_ISO = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data_list = search_news({'timestamp': date_to_ISO})
        return [(news['title'], news['url']) for news in data_list]

    except ValueError:
        raise ValueError("Data inválida")




# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
