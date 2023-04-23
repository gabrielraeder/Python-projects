from database.connection import db
import copy


class Mongo:
    @staticmethod
    def create(data, store):
        print(data)
        db[store].insert_many(copy.deepcopy(data))

    @staticmethod
    def insert_or_update(product, store):
        return (
            db[store]
            .update_one(
                {"url": product["url"]}, {"$set": product}, upsert=True
            )
            .upserted_id
            is not None
        )

    @staticmethod
    def find_all(store):
        return list(db[store].find({}, {"_id": False}))

    @staticmethod
    def search(query, store):
        return list(db[store].find(query))

    @staticmethod
    def get_collection(store):
        return db[store]
