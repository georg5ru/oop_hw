class Product:
    name: str
    description: str
    price: int
    quantity: int
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    name: str
    description: str
    products: list
    amount_products = len(products)
    def __init__(self, name, description, products, amount_categories, amount_products):
        self.name = name
        self.description = description
        self.products = products
        self.amount_categories = amount_categories
        self.amount_products = amount_products