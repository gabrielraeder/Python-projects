from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report_str = super().generate(products)
        products_by_company = super().products_quantity_by_company(products)
        string = ""
        for key, value in products_by_company.items():
            string += f"- {key}: {value}\n"

        return (
            f"{simple_report_str}\n"
            "Produtos estocados por empresa:\n"
            f"{string}"
        )
