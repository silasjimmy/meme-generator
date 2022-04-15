import random
import os
import requests
from flask import Flask, render_template, abort, request
from quoteengine.ingestor import Ingestor
from memegenerator.memeengine import MemeEngine

app = Flask(__name__, static_folder="static")

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    # Extract the filename instead in order to use
    # with url_for() in the template
    filename = path.split('/')[-1]
    return render_template('meme.html', path=filename)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    data = request.form
    image_url = data.get('image_url')
    body = data.get('body')
    author = data.get('author')

    try:
        # Download the image
        response = requests.get(image_url, stream=True)

        # Check if the file is an image
        file_type = response.headers.get('Content-Type').split('/')[0]
        if file_type != 'image':
            raise Exception("Invalid file format!")

        # Save the image
        temp_folder = os.path.join(os.getcwd(), 'tmp')
        os.makedirs(temp_folder, exist_ok=True)

        image_path = os.path.join(temp_folder, 'meme-img.jpg')
        with open(image_path, 'wb') as file:
            for block in response.iter_content(1024):
                if not block:
                    break

                file.write(block)

        path = meme.make_meme(image_path, body, author)

        # Delete the temporary image
        os.remove(image_path)
    except Exception as e:
        print("Something went wrong!", e)

    # Extract the filename instead in order to use
    # with url_for() in the template
    if path:
        filename = path.split('/')[-1]
    else:
        filename = None
    return render_template('meme.html', path=filename)


if __name__ == "__main__":
    app.run()
