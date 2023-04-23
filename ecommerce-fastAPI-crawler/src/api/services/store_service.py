from .aggregator import get_many_products_from_many_sites
from api.models.store_model import StoresModel


class StoresService:
    def __init__(self, model=StoresModel()) -> None:
        self.__model = model
        self.__stores = ["dell", "kabum", "americanas", "pichau"]

    def filter_by_store(self, products, store_name):
        filtered_products = [
            {"name": product.name, "price": product.price, "url": product.url}
            for product in products
            if product.url.__contains__(store_name)
        ]
        for product in filtered_products:
            self.__model.insert_or_update(product, store_name)

    def scrape(self, search_term, quantity):
        products = get_many_products_from_many_sites(search_term, quantity)
        if not products:
            return []

        for store in self.__stores:
            self.filter_by_store(products, store)

        return [
            product
            # f"{product.name = }\n{product.price = }\n{product.url = }\n"
            for product in sorted(products, key=lambda prod: prod.price)
        ]
