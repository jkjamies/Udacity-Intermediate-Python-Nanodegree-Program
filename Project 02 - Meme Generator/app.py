"""Implementation for main app and for flask."""

import random
import os
import requests
from flask import Flask, render_template, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        if Ingestor.parse(file) is not None:
            quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, image) for image in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form['body']
    author = request.form['author']
    image = requests.get(image_url)
    path=None
    try:
        tmp_file = f'tmp/{random.randint(0, 1000)}.jpg'
        with open(tmp_file, 'wb') as file:
            file.write(image.content)
        path = meme.make_meme(tmp_file, body, author)
    except:
        print('Failed to generate meme')
        if os.path.exists(tmp_file):
            os.remove(tmp_file)
        return render_template('meme_form.html')

    if os.path.exists(tmp_file):
        os.remove(tmp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
