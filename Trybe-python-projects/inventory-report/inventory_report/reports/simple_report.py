from datetime import datetime


class SimpleReport:
    @staticmethod
    def find_oldest(products, key: str):
        dates = [
            datetime.strptime(product[key], "%Y-%m-%d") for product in products
        ]
        return str(min(dates)).split(" ")[0]

    @staticmethod
    def find_next_expiration(products, key: str):
        dates = [
            datetime.strptime(product[key], "%Y-%m-%d") for product in products
        ]
        old = max(dates)
        for data in dates:
            if data < old and data > datetime.now():
                old = data
        return str(old).split(" ")[0]

    @staticmethod
    def products_quantity_by_company(products):
        obj = {}
        for product in products:
            if product["nome_da_empresa"] not in obj:
                obj[product["nome_da_empresa"]] = 0
            obj[product["nome_da_empresa"]] += 1
        return obj

    @classmethod
    def generate(cls, products):
        oldest = SimpleReport.find_oldest(products, "data_de_fabricacao")
        next_valid_date = SimpleReport.find_next_expiration(
            products, "data_de_validade"
        )
        company_quantity = SimpleReport.products_quantity_by_company(products)
        company_max_products = sorted(
            company_quantity.items(),
            key=lambda item: item[1],
            reverse=True,
        )[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {next_valid_date}\n"
            f"Empresa com mais produtos: {company_max_products}"
        )
