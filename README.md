# Motivational meme generator app
A simple Python application to generate both random and custom motivational memes from images and short quotes, using a commandline interface and a graphical interface. The commandline interface saves the memes locally to a disk while the graphical inteface is served with the Flask web framework.

## Getting started
1. Clone the project using:
```sh
git clone https://github.com/silasjimmy/meme-generator.git
```

2. Create a virtual environment and install the dependencies by running:
```sh
pip install -r requirements.txt
```

Before you continue ensure that ```Xpdf``` is also installed in your computer. It contains the pdftotext utility which is used in the project but not contained in the dependencies list. Visit this [link](https://www.xpdfreader.com/) for more information.

3. To use the CLI:
```sh
$ python3 meme.py -h

usage: meme.py [-h] [-path PATH] [-body BODY] [-author AUTHOR]

Generate a motivational meme

optional arguments:
  -h, --help      show this help message and exit
  -path PATH      path to the meme image
  -body BODY      the body of the quote
  -author AUTHOR  the author of the quote
```

or run the command below:

```sh
python3 meme.py
```

to generate a random meme

4. To use the web interface, run:
```sh
export FLASK_APP=app.py
```

```
flask run
```

### Development mode with Flask
For development purposes, make sure to add the following variables:

```sh
export FLASK_DEBUG=True
export FLASK_ENV=development
```

and run:

```sh
flask run --reload
```

for hot reloads whenever you make changes to the code.

Once the server starts, visit [this link](http://127.0.0.1:5000) using your favorite browser.

## Modules and dependencies
The project is made up of two modules and several dependencies.

### Dependencies
1. ```Flask``` - to build the web interface. Visit this [link](https://flask.palletsprojects.com/en/2.1.x/) for more information.
2. ```Pillow``` - for manipulating images. Visit this [link](https://pillow.readthedocs.io/en/stable/) for more information.
3. ```pandas``` - for extracting text content from csv documents. Visit this [link](https://pandas.pydata.org/) for more information.
4. ```python-docx``` - for extracting text content from docx documents. Visit this [link](https://python-docx.readthedocs.io/en/latest/) for more information.

### Modules
1. ```quoteengine``` module - deals with extracting and parsing quotes from txt, docx, pdf and csv documents.

Contains the ```ingestor``` and ```quote``` submodules.

- ```ingestor```
```Ingestor``` class: extract text content (quotes) from documents. Documents supported include txt, pdf, docx and csv.
**Methods**: *parse(path: str)* - parses the contents in the document referenced in the ```path ```. Returns a list of ```QuoteModel``` objects.

**Example**:
```sh
from quoteengine.ingestor import Ingestor

path = 'path/to/quotes/documents.txt'
quotes = Ingestor().parse(path)
print(type(quotes))

>>> <class 'list'>
```

- ```quote```
```QuoteModel``` class: instantiate quote objects.

**Attributes**: *body (str), author(str)*
```body``` - The quote's text
```author``` - The quote's author

**Example**:
```sh
from quoteengine.quote import QuoteModel

body = 'To be or not to be'
author = 'Wiseman'

quote = QuoteModel(body, author)
print(quote)

>>> "To be or not to be" - Wiseman
```

2. ```memegenerator``` module - deals with the creation and storing of the memes.

Contains the ```memeengine``` submodule.

- ```memeengine```
```MemeEngine``` class: create memes from an image and a quote.

**Attributes**: *output_dir (str)*

**Methods**: *make_meme(img_path: str, text: str, author: str, width: int)* - creates a meme using an image specified in ```img_path``` and a quote from text and author. The meme is resized to size width. Returns the path of the created meme in the disk (for CLI) or the relative path to the static files folder (for GUI).

**Example**:
```sh
from memegenerator.memeengine import MemeEngine

output_directory = 'memes'

img_path = '/path/to/the/image.jpg'
body = 'To be or not to be'
author = 'Wiseman'

quote = MemeEngine(output_directory).make_meme(img_path, body, author, 300)
print(quote)

>>> "/path/to/the/created/memes/meme.jpg"
```

## Author
- Silas Jimmy

## Credits
- [Udacity](https://www.udacity.com)

