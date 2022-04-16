"""This module generates memes by adding quotes to images."""

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint


class MemeEngine:
    """Class to create memes from images and quotes"""

    def __init__(self, output_dir: str) -> None:
        """Initialize a meme generator object."""
        self.output_dir = output_dir

    def make_meme(self,
                  img_path: str,
                  text: str,
                  author: str,
                  width=500) -> str:
        """Make a meme from an image and a quote.

        Arguments:
            img_path (str): path to the meme image
            text (str): quote's text
            author (str): quote's author
            width (int): image size of the meme

        Returns:
            meme_path (str): path to the generated meme
        """
        memes_folder = os.path.join(os.getcwd(), self.output_dir)

        # Create the output directory if it does not exist
        os.makedirs(memes_folder, exist_ok=True)

        try:
            with Image.open(img_path) as meme_image:
                # Create a name for the meme
                img_path_name = os.path.splitext(img_path)[0]
                meme_name = img_path_name.split('/')[-1]
                meme_name = meme_name + '_meme.png'

                # Resize the image
                width_percentage = width / float(meme_image.size[0])
                height = int(
                    float(meme_image.size[1]) * float(width_percentage))
                meme_image = meme_image.resize((width, height),
                                               Image.ANTIALIAS)

                # Draw the quote to the meme image
                text_font = ImageFont.truetype(
                    os.path.join(os.getcwd(), 'fonts/playfair-black.otf'), 26)
                author_font = ImageFont.truetype(
                    os.path.join(os.getcwd(), 'fonts/playfair-bold.otf'), 20)
                meme = ImageDraw.Draw(meme_image)

                # Generate random text anchor
                y_anchor = randint(20, meme_image.size[0] - 100)
                x_spacing = 25
                y_spacing = 35

                meme.text((20, y_anchor),
                          text, (0, 0, 0),
                          font=text_font,
                          stroke_fill=(255, 255, 255),
                          stroke_width=2)
                meme.text((20 + x_spacing, y_anchor + y_spacing),
                          f"- {author}", (0, 0, 0),
                          font=author_font,
                          stroke_fill=(255, 255, 255),
                          stroke_width=1)

                # Save the meme
                meme_path = os.path.join(memes_folder, meme_name)
                meme_image.save(meme_path)

            return meme_path
        except Exception as e:
            print(e)
