from api.services.store_service import StoresService


class StoresController:
    def __init__(self, news_service=StoresService()):
        self.service = news_service

    def scrape(self, search_term, quantity):
        return self.service.scrape(search_term, quantity)
