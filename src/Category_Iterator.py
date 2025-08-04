class CategoryIterator:
    def __init__(self, prod_obj) -> None:
        """Метод для инициализации экземпляра класса."""
        self.pr = prod_obj
        self.index = 0

    def __iter__(self):
        """Метод для вызова итерации"""
        self.index = 0
        return self

    def __next__(self):
        """Метод для вызова итерации"""
        if self.index < len(self.pr.products_in):
            prods = self.pr.products_in[self.index]
            self.index += 1
            return prods
        else:
            raise StopIteration
