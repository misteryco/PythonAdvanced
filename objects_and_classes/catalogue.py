class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.product_name = None

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [element for element in self.products if element[0] == first_letter]

    def __repr__(self):
        result = f'Items in the {self.name} catalogue:\n'
        self.sorted = sorted(self.products)
        for index in range(len(self.sorted)):
            if index < (len(self.sorted) - 1):
                result += f"{self.sorted[index]}\n"
            else:
                result += f'{self.sorted[index]}'
                return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
