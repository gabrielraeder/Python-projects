import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            if not path.endswith(".xml"):
                raise FileNotFoundError
            with open(path, encoding="utf8") as file:
                my_xml = file.read()
            my_dict = xmltodict.parse(my_xml)
            return my_dict["dataset"]["record"]
        except FileNotFoundError:
            raise ValueError("Arquivo inválido")
