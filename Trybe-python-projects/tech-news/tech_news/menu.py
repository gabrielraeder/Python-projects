import sys
from time import sleep
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


class InputChosen:
    def __init__(self) -> None:
        self.choice = 0
        self.__options = {
            "0": self.__input_zero,
            "1": self.__input_one,
            "2": self.__input_two,
            "3": self.__input_three,
            "4": self.__input_four,
            "5": self.__input_five,
        }

    def __input_handler(self):
        return input(
            """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair;
 ------------------------------------
 DIGITE: """
        ).rstrip()

    def chosen(self):
        self.choice = self.__input_handler()
        print("=" * 50)
        return self.__options[self.choice]()

    def __input_zero(self):
        return get_tech_news(
            int(input("Digite quantas notícias serão buscadas:"))
        )

    def __input_one(self):
        return search_by_title(input("Digite o título:"))

    def __input_two(self):
        return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))

    def __input_three(self):
        return search_by_category(input("Digite a categoria:"))

    def __input_four(self):
        return top_5_categories()

    def __input_five(self):
        return "Encerrando script\n"


# Requisitos 11 e 12
def analyzer_menu():
    inputChosen = InputChosen()
    try:
        while inputChosen.choice != "5":
            print(inputChosen.chosen())
            print("=" * 50)
            sleep(2)
    except KeyError:
        sys.stderr.write("Opção inválida\n")
