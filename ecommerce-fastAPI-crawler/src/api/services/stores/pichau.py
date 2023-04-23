from api.services.stores.website import Website
import requests

from api.services.utils import PRICE_REGEX


class Pichau(Website):
    def __init__(self) -> None:
        self.__base_url = "https://www.pichau.com.br"
        self.__search_url = f"{self.__base_url}/search"

    def _get_search_page_with_search_results(self, product_name: str):
        search_term = product_name.lower().replace(" ", "%20")
        return requests.get(
            self.__search_url,
            headers=super().HEADER,
            params={"q": search_term},
        ).text

    def _get_products_html(self, name: str):
        page = self._get_search_page_with_search_results(name)
        soup = super().beautify(page)
        products = soup.find_all("a", {"data-cy": "list-product"})
        return [str(product) for product in products if products]

    def _get_product_name(self, product_html: str):
        soup = super().beautify(product_html)
        return soup.find("h2").text

    def _get_product_price(self, product_html: str):
        soup = super().beautify(product_html)
        price = soup.find("div", {"class": "jss83"}).text
        try:
            price_str = PRICE_REGEX.search(price)
            string_num = price_str.group(0).replace(",", "")
            return float(string_num)
        except (AttributeError, ValueError, AttributeError) as err:
            return err

    def _get_product_url(self, product_html: str):
        soup = super().beautify(product_html)
        url = soup.find("a", {"data-cy": "list-product"})["href"]
        return self.__base_url + url
