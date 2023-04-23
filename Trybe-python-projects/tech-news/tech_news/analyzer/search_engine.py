from tech_news.database import search_news
from datetime import datetime


def transform_dict_list_into_tuples(lista):
    return [(item["title"], item["url"]) for item in lista]


# Requisito 7
def search_by_title(title):
    db_return = search_news({"title": {"$regex": title.lower()}})
    return transform_dict_list_into_tuples(db_return)


# Requisito 8
def search_by_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        db_return = search_news({"timestamp": format_date})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return transform_dict_list_into_tuples(db_return)


# Requisito 9
def search_by_category(category: str):
    db_return = search_news({"category": category.capitalize()})
    return transform_dict_list_into_tuples(db_return)
