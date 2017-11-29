from models import *

# Define products
pomme = Produit("Pomme", 0.60)
orange = Produit("Orange", 1.25)

def display(): # Display information
    print("Shopping Cart \n")
    print("Nos produits : ")
    print("Pomme : 0.60$")
    print("Orange : 1.25$ \n")
    print("Entrez les produits à acheter ex: pomme pomme orange pomme")

def processInput(user_input): # Converts user input to string list
    return [p for p in user_input.split()]

def addItemsToCart(cart, items):
    for item in items:
        if item.lower() == "pomme":
            cart.ajouterProduit(pomme)
        elif item.lower() == "orange":
            cart.ajouterProduit(orange)


display()
user_input = input("=> ")

items = processInput(user_input)

cart = Cart() # Create shopping cart

addItemsToCart(cart, items)

total = Caisse.calculerTotal(cart) # Get Total

print("Le prix total est : {} $".format(total)) # Displays result