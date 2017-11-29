class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Cart:
    produits = []
    def ajouterProduit(self, produit : Produit):
        self.produits.append(produit)

class Caisse:
    @staticmethod
    def calculerTotal(cart):
        total = 0
        for produit in cart.produits:
            total += produit.prix
        return round(total, 2)