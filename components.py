# CLASSES AND METHODS
class Store():
    def __init__(self, name):
       self.name = name
       self.products =  []

    def add_product(self, product):
        self.products.append(product)
        

    def print_products(self):
        print self.products


class Product():
    def __init__(self, name, description, price):
        self.name = name 
        self.description = description 
        self.price = price 

    def __str__(self):
        return "Product Name: %s\n product Description: %s\nPrice: %s KWD" %(self.name, self.description, self.price)


class Cart():
    def __init__(self):
       self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
       price = 0 
       for product in self.products
            price += product.price
            return price 

    def print_receipt(self):
        for products in add_to_cart 
            print (product) 
            print (get_total_price())

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
