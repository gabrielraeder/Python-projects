from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path, type: str):
        result = self.importer.import_data(path)
        for item in result:
            self.data.append(item)
        # ou
        #     self.data += list(new_data)
        # ou
        #     self.data = [*self.data, *data]
        # ou
        #     self.data.extend(new_data)

    def __iter__(self):
        return InventoryIterator(self.data)
