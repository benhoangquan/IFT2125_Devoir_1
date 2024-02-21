# Hoang Quan Tran, 20249088
# Richard Gu, 20211389

# this class is used to create the game cards in the cartes.txt file

from random import shuffle  # for mixing symbols on each card


class Generator:
    def __init__(self, order=7):
        self.order = order

    def generate_directions(self):
        """
        This function generates all possible directions for the projection diagonal.
        :return list of tuples of 2 integers:

        """
        directions = [(i, 1) for i in range(0, self.order)]
        directions.append((1, 0))
        return directions

    def convert_cartesian_to_index(self, cartesian_tuple):
        """
        This function converts a cartesian point to an index (of 1d array) in the card list.
        :param cartesian_tuple:
        :return:
        """
        return cartesian_tuple[1] * self.order + cartesian_tuple[0]

    def get_next_cartesian(self, cartesian_tuple, direction):
        """
        This function returns the next cartesian point after moving in the given direction.
        :param cartesian_tuple:
        :param direction:
        :return next cartesian point as a tuple of 2 integers:
        """
        x = (cartesian_tuple[0] + direction[0]) % self.order
        y = (cartesian_tuple[1] + direction[1]) % self.order
        return x, y

    def test_get_next_cartesian(self):
        self.order = 7
        assert self.get_next_cartesian((6, 2), (3, 1)) == (2, 3)
        assert self.get_next_cartesian((2, 3), (3, 1)) == (5, 4)
        self.order = 5
        assert self.get_next_cartesian((2, 2), (3, 1)) == (0, 3)
        assert self.get_next_cartesian((2, 3), (3, 1)) == (0, 4)

    def group_cards_by_direction(self, direction):
        """
        This functions groups cards by direction.
        All points in the same lime are grouped into a subgroup together.
        Different subgroups (parallel lines) are grouped into a groups of the same direction.
        :param direction: tuple of 2 integers
        :return:
        2d list of groups of subgroups of cards.
        Each subgroup is a list of points that are in the same line.
        """
        groups = []
        sub_group_by_line = []
        start_case = [(i, 0) for i in range(self.order)] if direction != (1, 0) \
            else [(0, i) for i in range(self.order)]

        for i in range(self.order):
            current_case = start_case[i]
            for j in range(self.order):
                current_case_idx = self.convert_cartesian_to_index(current_case)
                sub_group_by_line.append(current_case_idx)
                current_case = self.get_next_cartesian(current_case, direction)
            groups.append(sub_group_by_line.copy())
            sub_group_by_line.clear()

        return groups

    def assign_symbol_by_group_to_card(self, symbol, idx_to_be_assigned, cards):
        """
        This function assigns a symbol to the list of cards using the index from group.
        :param symbol: Symbol to be assigned
        :param idx_to_be_assigned: G
        :param cards:
        """
        for i in idx_to_be_assigned:
            cards[i].append(symbol)

    def test_group_cards(self):
        self.order = 2
        assert self.group_cards_by_direction((1, 0)) == [[0, 1], [2, 3]]
        assert self.group_cards_by_direction((0, 1)) == [[0, 2], [1, 3]]
        assert self.group_cards_by_direction((1, 1)) == [[0, 3], [1, 2]]

        self.order = 3
        assert self.group_cards_by_direction((1, 0)) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        assert self.group_cards_by_direction((0, 1)) == [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        assert self.group_cards_by_direction((1, 1)) == [[0, 4, 8], [1, 5, 6], [2, 3, 7]]
        assert self.group_cards_by_direction((2, 1)) == [[0, 5, 7], [1, 3, 8], [2, 4, 6]]

        self.order = 5
        assert self.group_cards_by_direction((1, 0)) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9],
                                                         [10, 11, 12, 13, 14], [15, 16, 17, 18, 19],
                                                         [20, 21, 22, 23, 24]]
        assert self.group_cards_by_direction((0, 1)) == [[0, 5, 10, 15, 20], [1, 6, 11, 16, 21],
                                                         [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24]]
        assert self.group_cards_by_direction((3, 1)) == [[0, 8, 11, 19, 22], [1, 9, 12, 15, 23],
                                                         [2, 5, 13, 16, 24], [3, 6, 14, 17, 20], [4, 7, 10, 18, 21]]

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        # generate directions
        directions = self.generate_directions()
        # generate symbols
        nb_symbols = self.order ** 2 + self.order + 1
        all_symbols = list(range(1, nb_symbols + 1))
        # generate cards
        main_cards = [[] for _ in range(self.order ** 2)]
        extra_cards = [[] for _ in range(self.order + 1)]

        # group by directions and loop by direction
        for i, direction in enumerate(directions):
            converging_card = extra_cards[i]  # reference?

            # group cards by direction
            groups = self.group_cards_by_direction(direction)
            for sub_group in groups:
                symbol = all_symbols.pop(0)
                self.assign_symbol_by_group_to_card(symbol, idx_to_be_assigned=sub_group, cards=main_cards)
                converging_card.append(symbol)

        # assign the last symbol to the extra_card groups
        symbol = all_symbols.pop(0)
        for card in extra_cards:
            card.append(symbol)

        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards
        # and writing cards in the cards_file file
        def to_string(card_list):
            return " ".join(list(map(str, card_list)))

        with open(cards_file, 'w') as f:
            for card in main_cards:
                # convert card to string
                shuffle(card)
                f.write(f'{to_string(card)}\n')

            for card in extra_cards:
                shuffle(card)
                f.write(f'{to_string(card)}\n')
