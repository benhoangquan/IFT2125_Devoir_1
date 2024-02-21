# Hoang Quan Tran, 20249088
# Richard Gu, 20211389

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

class Verificator:
    def __init__(self):
        pass

    def verify(self, cards_file="cartes.txt", verbose=False):
        """
        Verifie la validite et l'optimalite du jeu de cartes
        :param cards_file: le fichier contenant les cartes
        :param verbose:
        :return:
        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide
        """

        if verbose:
            print("***Verification des cartes***")

        # ouvrir fichier et lire les cartes
        try:
            f = open(cards_file, 'r')
            cards = []
            for line in f.readlines():
                cardInfo = line.strip().split()
                cards.append(cardInfo)

        except FileNotFoundError:
            print("Erreur: Le fichier n'existe pas!!!")
            return 2

        nb_cards = len(cards)  # nb de cartes
        order = len(cards[1]) - 1  # ordre = nombre symboles/carte -1

        # test : le nombre de carte devrait être optimal
        if order ** 2 + order + 1 != nb_cards:
            return 1

        # test : le nombre de symboles par carte est le même pour chaque carte
        nb_symbol = len(cards[1])
        for card in cards:
            if len(card) != nb_symbol:
                if verbose:
                    print("Nombre de symboles par carte pas constant!!!")
                return 2

        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
        for i in range(nb_cards):  # numCards = nb de cartes
            card_to_verify = cards[i]
            for j in range(i + 1, nb_cards):  # for each other card from i to the end:
                count = [0] * (order + 1)  # ex pour ordre 3: [1,2,3,4] => 4 carte a verifier
                for s in range(order + 1):  # for each symbol in carteAverifier:
                    for s2 in range(order + 1):  # for each symbol of the other card:
                        if card_to_verify[s] == cards[j][s2]:
                            count[s] += 1

                if sum(count) != 1:
                    if verbose:
                        print("Pas un seul symbole en commun par paire!!!")
                    return 2

        # test : le nombre de symbole total devrait être optimal
        symbol_list = []
        for card in cards:
            for symbol in card:
                if symbol not in symbol_list:
                    symbol_list.append(symbol)

        if order ** 2 + order + 1 != len(symbol_list):
            if verbose:
                print("Nombre de symbole total non optimal!!!")
            return 1

        return 0
