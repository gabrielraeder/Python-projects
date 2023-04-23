import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            with open(path, encoding="utf8") as file:
                content = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = content
            return [
                {header[index]: item for index, item in enumerate(value)}
                for value in data
            ]
        except (FileNotFoundError, IndexError):
            raise ValueError("Arquivo inválido")
