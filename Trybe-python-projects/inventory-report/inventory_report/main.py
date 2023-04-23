import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def inventory_loader(path):
    if path.endswith(".csv"):
        return InventoryRefactor(CsvImporter)
    elif path.endswith(".json"):
        return InventoryRefactor(JsonImporter)
    elif path.endswith(".xml"):
        return InventoryRefactor(XmlImporter)


def report_type(tipo, data):
    if tipo == "simples":
        sys.stdout.write(SimpleReport.generate(data))
    elif tipo == "completo":
        sys.stdout.write(CompleteReport.generate(data))


def main():
    try:
        _, path, tipo = sys.argv
        result = inventory_loader(path)

        result.import_data(path, tipo)
        report_type(tipo, result.data)

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
