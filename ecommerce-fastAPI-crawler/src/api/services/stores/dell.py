from api.services.stores.website import Website
import requests

from api.services.utils import PRICE_REGEX


class Dell(Website):
    def __init__(self) -> None:
        self.__base_url = "https:"
        self.__search_url = f"{self.__base_url}//www.dell.com/pt-br/search/"

    def _get_search_page_with_search_results(self, product_name: str):
        search_term = product_name.lower().replace(" ", "%20")
        return requests.get(
            self.__search_url + search_term, headers=super().HEADER
        ).text

    def _get_products_html(self, name: str):
        page = self._get_search_page_with_search_results(name)
        soup = super().beautify(page)
        products = soup.find_all("section", {"class": "ps-top"})
        return [str(product) for product in products if products]

    def _get_product_name(self, product_html: str):
        soup = super().beautify(product_html)
        return soup.find("h3", {"class": "ps-title"}).a.text

    def _get_product_price(self, product_html: str):
        soup = super().beautify(product_html)
        price: str = soup.find("div", {"class": "ps-dell-price"}).text
        try:
            price_str = PRICE_REGEX.search(price)
            string_num = price_str.group(0).replace(".", "").replace(",", ".")
            return float(string_num)
        except (AttributeError, ValueError, AttributeError) as err:
            return err

    def _get_product_url(self, product_html: str):
        soup = super().beautify(product_html)
        url = soup.find("h3", {"class": "ps-title"}).a["href"]
        return self.__base_url + url
