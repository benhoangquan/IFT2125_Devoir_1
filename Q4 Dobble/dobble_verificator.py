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



            
        try:                 #ouvrir fichier et lire les cartes
            f = open(cards_file, 'r')
            cards=[]
            for line in f.readlines():
                cardInfo = line.strip().split()
                cards.append(cardInfo)

        except FileNotFoundError:
            print("Erreur: Le fichier n'existe pas!!!")
            return 2

        numCards = len(cards)            #nb de cartes

        order = len(cards[1]) - 1         #ordre = nombre symboles/carte -1


        #########################################################################################
        
        # test : le nombre de carte devrait être optimal
        if (order)**2 + order + 1 != numCards:   
           
            return 1

        # test : le nombre de symboles par carte est le même pour chaque carte
        numSymb= len(cards[1])
        for card in cards:
            if len(card) != numSymb:
                if verbose:
                    print("Nombre de symboles par carte pas constant!!!")
                return 2 

        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun

        for i in range(numCards):    #numCards = nb de cartes  
            carteAVerifier = cards[i]
            for j in range (i+1, numCards):    #for each other card from i to the end:

                count = [0]*(order+1)  #ex pour ordre 3: [1,2,3,4] => 4 carte a verifier
                for s in range(order+1):    #for each symbol in carteAverifier:
                    for s2 in range(order+1):  #for each symbol of the other card:
                        if carteAVerifier[s] == cards[j][s2]:
                            count[s] += 1
                if sum(count) != 1:     
                    if verbose:
                        print("Pas un seul symbole en commun par paire!!!")
                    return 2
                    

        # test : le nombre de symbole total devrait être optimal
        listSymb = []
        for card in cards:
            for symb in card:
                if symb not in listSymb:
                    listSymb.append(symb)
        if order**2 + order + 1 != len(listSymb):
            if verbose:
                print("Nombre de symbole total non optimal!!!")
            return 1
    

                
        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide
        return 0

        
