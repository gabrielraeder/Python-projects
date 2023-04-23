import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        try:
            if not path.endswith(".json"):
                raise FileNotFoundError
            with open(path, encoding="utf8") as file:
                content = json.load(file)
            return content
        except FileNotFoundError:
            raise ValueError("Arquivo inválido")
