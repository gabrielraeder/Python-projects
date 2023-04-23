from api.database.mongodb import db
import copy


class NewsMongo:
    @staticmethod
    def create_news(data):
        db.news.insert_many(copy.deepcopy(data))

    @staticmethod
    def insert_or_update(notice):
        return (
            db.news.update_one(
                {"url": notice["url"]}, {"$set": notice}, upsert=True
            ).upserted_id
            is not None
        )

    @staticmethod
    def find_news():
        return list(db.news.find({}, {"_id": False}))

    @staticmethod
    def search_news(query):
        return list(db.news.find(query))

    @staticmethod
    def get_collection():
        return db.news
