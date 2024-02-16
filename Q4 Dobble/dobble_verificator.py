#Nom, Matricule
#Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")
        # TODO
        # a completer

        # test : le nombre de carte devrait être optimal
        # test : le nombre de symboles par carte est le même pour chaque carte
        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
        # test : le nombre de symbole total devrait être optimal
            
        # test: the number of cards should be optimal
        # test: the number of symbols per card is the same for each card
        # test: each pair of cards always shares one and only one symbol in common
        # test: the total number of symbols should be optimal



        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide
            
        # success (0) if the game is valid and optimal
        # warning (1) if the card game is not optimal
        # error (2) if the card set is invalid
        return 0

        
