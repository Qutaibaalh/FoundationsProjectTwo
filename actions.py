# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.LazyShop.com"  

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % www.LazyShop.com)

def print_stores():
    for store in stores 
        print ("- %s" % store.name)

def get_store(store_name):
    for store in stores 
        if store.name == store_name:
            return store 
        else: 
            return False 

def pick_store():
    print_stores()
    print ()

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
