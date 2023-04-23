from datetime import datetime
from api.models.news_model import NewsModel
from api.utils.scraper import NewsScraper


class NewsService:
    def __init__(self, model=NewsModel()):
        self.model = model
        self.scraper = NewsScraper

    def removes_repeated(self, links, amount):
        repeated = [
            link
            for link in links
            if self.model.search_news_model({"url": link})
        ]
        return [link for link in links if link not in repeated]

    def create_news_db(self, links, amount):
        remove_repeated = self.removes_repeated(links, amount)
        news = [
            self.scraper.scrape_news(self.scraper.fetch(link))
            for link in remove_repeated[:amount]
        ]
        try:
            self.model.create_news_model(news)
        except TypeError:
            return ""
        return news

    def get_tech_news(self, amount):
        page = self.scraper.fetch("https://blog.betrybe.com/")
        all_links = self.scraper.scrape_updates(page)
        next_link = self.scraper.scrape_next_page_link(page)
        while len(all_links) < amount:
            next_page = self.scraper.fetch(next_link)
            new_page_links = self.scraper.scrape_updates(next_page)
            all_links.extend(new_page_links)
            next_link = self.scraper.scrape_next_page_link(next_page)
        return self.create_news_db(all_links, amount)

    @staticmethod
    def transform_dict_list_into_tuples(lista):
        return [(item["title"], item["url"]) for item in lista]

    def search_by_title(self, title):
        db_return = self.model.search_news_model(
            {"title": {"$regex": title, "$options": "i"}}
        )
        return NewsService.transform_dict_list_into_tuples(db_return)

    def search_by_date(self, date):
        try:
            format_date = datetime.strptime(date, "%Y-%m-%d").strftime(
                "%d/%m/%Y"
            )
            db_return = self.model.search_news_model(
                {"timestamp": format_date}
            )
        except ValueError:
            raise ValueError("Data inválida")
        else:
            return NewsService.transform_dict_list_into_tuples(db_return)

    def search_by_category(self, category: str):
        db_return = self.model.search_news_model(
            {"category": {"$regex": f"^{category}$", "$options": "i"}}
        )
        return NewsService.transform_dict_list_into_tuples(db_return)

    def top_5_categories(self):
        db_return = self.model.search_news_model({})
        categories = {}
        for item in db_return:
            if item["category"] not in categories:
                categories[item["category"]] = 0
            categories[item["category"]] += 1
        sorting = sorted(categories.items(), key=lambda item: item[0])
        sorting2 = sorted(sorting, key=lambda item: item[1], reverse=True)
        return [category[0] for category in sorting2][:5]
