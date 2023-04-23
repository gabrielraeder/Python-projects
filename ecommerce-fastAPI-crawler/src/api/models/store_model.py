from database.mongo import Mongo
from api.models.model import Model


class StoresModel(Model):
    def __init__(self, database=Mongo):
        self.__database = database

    def create(self, data, store):
        return self.__database.create(data, store)

    def insert_or_update(self, product, store):
        return self.__database.insert_or_update(product, store)

    def find_all(self, store):
        return self.__database.find_all(store)

    def search(self, query, store):
        return self.__database.search_news(query, store)

    def get_collection(self, store):
        return self.__database.get_collection(store)
