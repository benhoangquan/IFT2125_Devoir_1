# Nom, Matricule
# Nom, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

from random import shuffle # pour le melange des symboles sur chaque carte # for mixing symbols on each card


# TODO
# - create nametuple instead of direction[1] and direction[0]


class Generator():
    def __init__(self, order=7):
        self.order = order
        self.main_cards = [[] for _ in range(order ** 2)]
        self.extra_cards = [[] for _ in range(self.order + 1)]

    def generate_directions(self):
        directions = [(i, 1) for i in range(0, self.order)]
        directions.append((1, 0))
        return directions

    def convert_cartesian_to_index(self, cartesian_tuple):
        return cartesian_tuple[1] * self.order + cartesian_tuple[0]

    def get_next_cartesian(self, cartesian_tuple, direction):
        x = (cartesian_tuple[0] + direction[0]) % self.order
        y = (cartesian_tuple[1] + direction[1]) % self.order
        return x, y

    def group_cards_by_direction(self, direction):
        groups = []
        sub_group = []
        start_case = [(i, 0) for i in range(self.order)] if direction != (1, 0) else [(0, i) for i in range(self.order)]
        # if direction 1, 0 then start case = 0,0; 0,1; 0,2; etc
        # if other direction then start case = 0,0; 1,0; 2,0; etc

        for i in range(self.order):
            current_case = start_case[i]
            for j in range(self.order):
                current_case_idx = self.convert_cartesian_to_index(current_case)
                sub_group.append(current_case_idx)
                current_case = self.get_next_cartesian(current_case, direction)
            groups.append(sub_group.copy())
            sub_group.clear()

        return groups

    def assign_symbol_to_group(self, group, symbol):
        # group example input: [0, 1, 2]
        for i in group:
            self.main_cards[i].append(symbol)

    def test_group_cards(self):
        self.order = 3
        assert self.group_cards_by_direction((1, 0)) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        assert self.group_cards_by_direction((0, 1)) == [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        assert self.group_cards_by_direction((1, 1)) == [[0, 4, 8], [1, 5, 6], [2, 3, 7]]
        assert self.group_cards_by_direction((2, 1)) == [[0, 5, 7], [1, 3, 8], [2, 4, 6]]

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        # generate directions
        directions = self.generate_directions()
        nb_directions = len(directions)
        # generate symbols
        nb_symbols = self.order ** 2 + self.order + 1
        all_symbols = list(range(nb_symbols))
        # generate cards

        # loop in all directions
        for i in range(nb_directions):
            direction = directions[i]
            converging_card = self.extra_cards[i] # reference?

            # group cards by direction
            groups = self.group_cards_by_direction(direction)
            for sub_group in groups:
                symbol = all_symbols.pop(0)
                self.assign_symbol_to_group(sub_group, symbol)
                converging_card.append(symbol)

        # assign the last symbol to the extra_card groups
        symbol = all_symbols.pop(0)
        for card in self.extra_cards:
            card.append(symbol)

        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards
        # and writing cards in the cards_file file
        to_string = lambda card_list: " ".join(list(map(str, card_list)))
        with open(cards_file, 'w') as f:
            for card in self.main_cards:
                # convert card to string
                f.write(f'{to_string(shuffle(card))}\n')

            for card in self.extra_cards:
                f.write(f'{to_string(shuffle(card))}\n')



if __name__ == "__main__":
    g = Generator(3)
    g.generate("test_cartes.txt")
