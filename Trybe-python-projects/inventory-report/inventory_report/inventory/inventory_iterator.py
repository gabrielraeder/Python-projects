from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __next__(self):
        try:
            target = self.data[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return target
