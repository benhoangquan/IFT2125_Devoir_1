# Hoang Quan Tran, 20249088
# Richard Gu, 20211389

# this class is used to create the game visual cards in the "results" folder

from PIL import Image, ImageOps
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

def parse_input_array(s):
    return list(map(int, str(s).strip().split(' ')))


class Creator:
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def calculate_coordinates(self, cells_per_side, pic_idx):
        '''
        Calculate the coordinates for each grid cell in a square grid given the index of the cell.
        :param cells_per_side:
        :param pic_idx:
        :return:
        '''
        # Calculate the size of a grid cell
        cell_size = self.pic_size / cells_per_side

        # Calculate the coordinates for each grid cell
        i = pic_idx // cells_per_side
        j = pic_idx % cells_per_side
        x = int(self.border_size + i * cell_size)
        y = int(self.border_size + j * cell_size)

        return x, y

    def make_cards(self, cards_file="cartes.txt", verbose=False):
        """
        Create the visual cards in png from the cards file and save them in the "results" folder
        :param cards_file: path to the file containing the cards
        :param verbose:
        :return:

        """

        if verbose:
            print("***Creation des cartes visuelles***")

        input_folder = "logo_scraper/logos"
        output_folder = "logo_results"

        with open(cards_file, "r") as f:
            card_id = 1
            while pic_id_array := f.readline():
                # parse the input array
                pic_id_array = parse_input_array(pic_id_array)

                # create a new background image
                image_layer = Image.new('RGBA', (self.pic_size, self.pic_size))
                for idx, pic_id in enumerate(pic_id_array):
                    # open the image
                    pic_to_paste = Image.open(f'{input_folder}/{pic_id}.png').convert("RGBA")

                    # calculate the parameters for image placement, rotation and resizing
                    cells_per_side = math.ceil(math.sqrt(len(pic_id_array)))
                    cell_size = int(self.pic_size / cells_per_side / math.sqrt(2))
                    x, y = self.calculate_coordinates(cells_per_side, idx)
                    pic_to_paste.thumbnail((cell_size, cell_size))

                    # new size while keeping the aspect ratio
                    angle = random.randint(0, 360)
                    new_width = int(abs(cell_size * math.cos(angle)) \
                                    + abs(cell_size * math.sin(angle)))
                    new_height = int(abs(cell_size * math.cos(angle)) \
                                 + abs(cell_size * math.sin(angle)))

                    # rotation and resize
                    pic_to_paste = pic_to_paste.rotate(angle, expand=True)
                    pic_to_paste = pic_to_paste.resize((int(new_width), int(new_height)))

                    # paste the image
                    # mask = Image.new("L", pic_to_paste.size, 0)
                    image_layer.paste(pic_to_paste, (x, y))

                # add white background
                background = Image.new('RGBA', image_layer.size, 'white')
                background.paste(image_layer, mask=image_layer)

                # add border
                background = ImageOps.expand(background, border=self.border_size, fill='black')
                background.save(f"{output_folder}/card{card_id}.png")
                card_id += 1

if __name__ == "__main__":
    c = Creator(300)
    c.make_cards("cartes.txt", verbose=True)