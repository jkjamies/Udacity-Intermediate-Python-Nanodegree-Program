"""Generate memes from image and quote."""

import pathlib
import random
import os
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Generate a meme using an image and quote."""

    def __init__(self, output_dir):
        """Set the output directory.

        Arguments:
            output_dir (str): Output directory to save meme.
        """
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate the meme from image and quote.

        Arguments:
            img_path (str): Path to the image file.
            text (str): Quote for the meme.
            author (str): Author of the quote for the meme.
            width (int): Width of the image (500 max and default).

        Returns:
            save_image_path (str): Path that the meme file was saved to.
        """
        try:
            image = self.load_image(img_path)
        except Exception as e:
            print(f'Exception: {e}')
        else:
            image = self.resize(image, width)
            image = self.add_quote_body(image, text, author)

            save_image_path = f'{self.output_dir}/{random.randint(0, 1000)}.jpg'
            image.save(save_image_path)
            print(f'Meme saved: {save_image_path}')

            return save_image_path

    def load_image(self, path: str):
        """Load the image.

        Arguments:
            path (str): Path to the image file.

        Returns:
            image: Image opened.
        """
        return Image.open(path)

    def resize(self, image, width: int):
        """Resize the image.

        Arguments:
            image: Image to resize.
            width (int): Width of the image.

        Returns:
            image: Image resized
        """
        if width is not None:
            ratio = width/float(image.size[0])
            height = int(ratio*float(image.size[1]))
            image = image.resize((width, height), Image.NEAREST)

        return image

    def add_quote_body(self, image, quote: str, author: str):
        """Add the quote and author to the image.

        Arguments:
            image: Image to resize.
            quote (str): Quote for the meme.
            author (str): Author of the quote for the meme.

        Returns:
            image: Image with quote and author added.
        """
        if quote and author:
            draw = ImageDraw.Draw(image)
            font_path = (pathlib.Path(__file__).parent.parent.absolute() / "fonts/times.ttf")
            font = ImageFont.truetype(str(font_path), 30, encoding="unic")

            draw.text((10, 30), f'{quote}\n- {author}', font=font, fill='white')

        return image
