import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_reader(path):
        try:
            with open(path, encoding="utf8") as file:
                content = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = content
            return [
                {header[index]: item for index, item in enumerate(value)}
                for value in data
            ]
        except FileNotFoundError:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def json_reader(path):
        try:
            with open(path, encoding="utf8") as file:
                content = json.load(file)
            return content
        except FileNotFoundError:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def xml_reader(path):
        try:
            with open(path, encoding="utf8") as file:
                my_xml = file.read()
            my_dict = xmltodict.parse(my_xml)
            return my_dict["dataset"]["record"]
        except FileNotFoundError:
            raise ValueError("Arquivo inválido")

    @staticmethod
    def read_file(path):
        if path.endswith(".csv"):
            return Inventory.csv_reader(path)
        elif path.endswith(".json"):
            return Inventory.json_reader(path)
        elif path.endswith(".xml"):
            return Inventory.xml_reader(path)

    @classmethod
    def import_data(cls, path: str, type: str):
        result = Inventory.read_file(path)
        if type == "simples":
            return SimpleReport.generate(result)
        elif type == "completo":
            return CompleteReport.generate(result)


# OUTRA FORMA DE FAZER
# import os

# report_types = {"simples": SimpleReport, "completo": CompleteReport}

# import_types = {
#     ".csv": CsvImporter,
#     ".json": JsonImporter,
#     ".xml": XmlImporter,
# }

# class Inventory:
#     @staticmethod
#     def import_data(file: str, type: str):
#         file_name, file_extension = os.path.splitext(file)
#         imported_file = import_types[file_extension].import_data(file)
#         return report_types[type].generate(imported_file)
