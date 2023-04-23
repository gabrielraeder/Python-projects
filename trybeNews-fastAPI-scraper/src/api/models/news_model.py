from api.database.news_mongo import NewsMongo


class NewsModel:
    def __init__(self, database=NewsMongo):
        self.__database = database

    def create_news_model(self, data):
        return self.__database.create_news(data)

    def insert_or_update_model(self, notice):
        return self.__database.insert_or_update(notice)

    def find_news_model(self):
        return self.__database.find_news()

    def search_news_model(self, query):
        return self.__database.search_news(query)

    def get_collection_model(self):
        return self.__database.get_collection()
