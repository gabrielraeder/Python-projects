from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def create(self, data, store):
        raise NotImplementedError

    @abstractmethod
    def insert_or_update(self, product, store):
        raise NotImplementedError

    @abstractmethod
    def find_all(self, store):
        raise NotImplementedError

    @abstractmethod
    def search(self, query, store):
        raise NotImplementedError

    @abstractmethod
    def get_collection(self, store):
        raise NotImplementedError
