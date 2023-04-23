from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    db_return = search_news({})
    categories = {}
    for item in db_return:
        if item["category"] not in categories:
            categories[item["category"]] = 0
        categories[item["category"]] += 1
    sorting = sorted(categories.items(), key=lambda item: item[0])
    sorting2 = sorted(sorting, key=lambda item: item[1], reverse=True)
    return [category[0] for category in sorting2][:5]
