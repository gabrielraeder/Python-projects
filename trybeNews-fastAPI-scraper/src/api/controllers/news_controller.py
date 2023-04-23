from api.services.news_service import NewsService


class NewsController:
    def __init__(self, news_service=NewsService()):
        self.service = news_service

    def scrape_news(self, amount):
        return self.service.get_tech_news(amount=amount)

    def title_search(self, title):
        return self.service.search_by_title(title)

    def category_search(self, category):
        return self.service.search_by_category(category)

    def date_search(self, date):
        return self.service.search_by_date(date)

    def top_categories(self):
        return self.service.top_5_categories()
