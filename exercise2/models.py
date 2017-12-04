import math

class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Cart:
    produits = []

    def ajouterProduit(self, produit: Produit):
        self.produits.append(produit)
    
    def empty(self):
        self.produits = []


class Caisse:
    @staticmethod
    def calculerTotal(cart, offre=False):
        total = 0

        if offre:
            # Offre =  qnt gratuite + qnt à acheter / qnt a acheter
            offrePomme = 2/1
            offreOrange = 3/2

            nbPomme = nbOrange = 0
            prixPomme = prixOrange = 0

            for produit in cart.produits:
                if produit.nom.lower() == "pomme":
                    nbPomme += 1
                    prixPomme = produit.prix
                elif produit.nom.lower() == 'orange':
                    nbOrange += 1
                    prixOrange = produit.prix
                else:
                    total += produit.prix

            # Calculer l'offre
            total += math.ceil(nbPomme / offrePomme) * prixPomme 
            total += math.ceil(nbOrange / offreOrange) * prixOrange
            
        else:
            for produit in cart.produits:
                total += produit.prix
        
        return round(total, 2)