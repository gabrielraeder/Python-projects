from api.services.stores.website import Website
import requests

from api.services.utils import PRICE_REGEX


class Kabum(Website):
    def __init__(self) -> None:
        self.__base_url = "https://www.kabum.com.br"
        self.__search_url = f"{self.__base_url}/busca/"

    def _get_search_page_with_search_results(self, product_name: str):
        search_term = product_name.lower().replace(" ", "-")
        return requests.get(
            self.__search_url + search_term, headers=super().HEADER
        ).text

    def _get_products_html(self, name: str):
        page = self._get_search_page_with_search_results(name)
        soup = super().beautify(page)
        products = soup.find_all("div", {"class": "productCard"})
        return [str(product) for product in products if products]

    def _get_product_name(self, product_html: str):
        soup = super().beautify(product_html)
        return soup.find("span", {"class": "nameCard"}).text

    def _get_product_price(self, product_html: str):
        soup = super().beautify(product_html)
        price: str = soup.find("span", {"class": "priceCard"}).text
        try:
            price_str = PRICE_REGEX.search(price)
            string_num = price_str.group(0).replace(".", "").replace(",", ".")
            return float(string_num)
        except (AttributeError, ValueError, AttributeError) as err:
            return err

    def _get_product_url(self, product_html: str):
        soup = super().beautify(product_html)
        url = soup.find("a", {"class": "sc-ff8a9791-10"})["href"]
        return self.__base_url + url
