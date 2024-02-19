# Nom, Matricule
# Nom, Matricule

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
        # Calculate the size of a grid cell
        cell_size = self.pic_size / cells_per_side

        # Calculate the coordinates for each grid cell
        i = pic_idx // cells_per_side
        j = pic_idx % cells_per_side
        x = int(self.border_size + i * cell_size)
        y = int(self.border_size + j * cell_size)

        return x, y

    def make_cards(self, cards_file="test_cartes.txt", verbose=False):
        if verbose:
            print("***Creation des cartes visuelles***")

        input_folder = "images"
        output_folder = "test_results"

        with open(cards_file, "r") as f:
            card_id = 1
            while pic_id_array := f.readline():
                # parse the input array
                pic_id_array = parse_input_array(pic_id_array)

                # create a new background image
                background = Image.new('RGBA', (self.pic_size, self.pic_size), 'white')
                for idx, pic_id in enumerate(pic_id_array):
                    # open the image
                    pic_to_paste = Image.open(f'{input_folder}/{pic_id}.png')

                    # calculate the parameters for image placement, rotation and resizing
                    cells_per_side = math.ceil(math.sqrt(len(pic_id_array)))
                    cell_size = int(self.pic_size / cells_per_side / math.sqrt(2))
                    x, y = self.calculate_coordinates(cells_per_side, idx)
                    pic_to_paste.thumbnail((cell_size, cell_size))

                    angle = random.randint(0, 360)
                    new_width = int(abs(pic_to_paste.width * math.cos(angle)) \
                                    + abs(pic_to_paste.height * math.sin(angle)))
                    new_height = int(abs(pic_to_paste.height * math.cos(angle)) \
                                 + abs(pic_to_paste.width * math.sin(angle)))

                    # rotation and resize
                    pic_to_paste = pic_to_paste.rotate(angle, expand=True, resample=Image.BICUBIC)
                    pic_to_paste = pic_to_paste.resize((int(new_width), int(new_height)))

                    # paste the image
                    background.paste(pic_to_paste, (x, y), mask=pic_to_paste)

                    # add border
                background = ImageOps.expand(background, border=self.border_size, fill='black')
                background.save(f"{output_folder}/card{card_id}.png")
                card_id += 1


if __name__ == "__main__":
    creator = Creator(600)
    creator.make_cards()