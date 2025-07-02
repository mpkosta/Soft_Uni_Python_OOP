from project.product import Product


class ProductRepository():#repository for all products delivered to the shop
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product: #return the whole object with the same name if found
        return next((product for product in self.products if product.name == product_name), None) #where is the product.name coming from??

    def remove(self, product_name: str) -> None:
        product = self.find(product_name) #find me the product name in the above method and remove it
        if product:
            self.products.remove(product)

    def __repr__(self):
        # return {"\n".join(map(repr, self.products))}
        return "\n".join([f'{p.name}: {p.quantity}' for p in self.products])