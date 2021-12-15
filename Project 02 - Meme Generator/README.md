# Meme Generator

## Overview

This project is a meme generator, the second project for the Intermediate Python Nanodegree program from Udacity. The python application can generate random memes from user input through command line interface and a web interface. It also has capability to take in user input to generate a meme on the web interface. Memes consist of an image, a quote, and an author.

## Setup

Create a venv with python 3 (3.9 used for project creation) and install the dependencies by running `pip install -r requirements.txt`.

## Using the Application Web Interface (Flask)

To use the application, run using `python app.py` or if multiple python versions are installed, `python3 app.py`. The web interface will run at http://127.0.0.1:5000/. Random will generate a random meme from the project contained images and quotes with author. The create button will take the user to a meme form to fill out desired image, quote, and author for meme generation. Ensure no other processes are running on port 5000, else you can run using `flask run --host 0.0.0.0 --port 3000` as an example.

## Using the Application Command Line Interface

Use the following cli commands to customize the meme generation from running `python meme.py` or if multiple python versions are installed, `python3 meme.py`:
  --path: Image file path
  --body: Quote to add to meme
  --author: Author of quote for meme
The resulting command should be formatted like `python meme.py --path [image path] --body [quote body] --author[quote author]`.

## Primary Modules

- `QuoteEngine`: uses ingestors to parse different file types for quotes and authors
- `MemeEngine`: uses `pillow` to create a meme with modified size and an added quote with author

## Sub-Modules

- Ingestors using `IngestorInterface` and `Ingestor` classes
    - `CSVIngestor`: ingests csv files
    - `DocxIngestor`: ingests docx files
    - `PDFIngestor`: ingests pdf files
    - `TextIngestor`: ingests txt files

- `QuoteModel`: used to model a quote with body and author