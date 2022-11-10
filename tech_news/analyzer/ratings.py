from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    db = get_collection()
    list = db.find().sort([("comments_count", -1), ("title", 1)]).limit(5)
    top_5 = [(news['title'], news['url']) for news in list]

    return top_5



# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
