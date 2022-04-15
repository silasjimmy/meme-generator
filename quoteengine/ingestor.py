"""This module encapsulates all ingestors to load text, docx, pdf and csv files"""

from abc import ABC, abstractmethod
from typing import List
from docx import Document
from pandas import read_csv
from quoteengine.quote import QuoteModel
import subprocess


class IngestorInterface(ABC):
    """Ingestor interface class definition."""
    file_extension = ''

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be ingested.

        Arguments:
            path (str): path to the file to ingest

        Returns:
            bool: True if the file can be ingested, False otherwise
        """
        return path.endswith(cls.file_extension)

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse.

        Arguments:
            path (str): path

        Returns:
            list: a list of QuoteModel objects
        """
        return []


class TextIngestor(IngestorInterface):
    """Class definition to import quotes from text documents."""
    file_extension = '.txt'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from text documents and create QuoteModel objects.
        Returns:
            quotes (list): list of QuoteModel objects
        """
        try:
            with open(path, 'r') as infile:
                contents = infile.read()
                contents = contents.split("\n")
                quotes = []

                for line in contents:
                    line = line.split("-")
                    if len(line) == 2:
                        body, author = tuple(line)
                        quote = QuoteModel(body.strip(), author.strip())
                        quotes.append(quote)

            return quotes
        except Exception as e:
            print(e)


class DocxIngestor(IngestorInterface):
    """Class definition to import quotes from docx documents."""
    file_extension = '.docx'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from docx documents and create QuoteModel objects.
        Returns:
            quotes (list): list of QuoteModel objects
        """
        try:
            document = Document(path)
            quotes = []

            for paragraph in document.paragraphs:
                line = paragraph.text.split("-")
                if len(line) == 2:
                    body, author = tuple(line)
                    quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(quote)

            return quotes
        except Exception as e:
            print(e)


class PDFIngestor(IngestorInterface):
    """Class definition to import quotes from pdf documents."""
    file_extension = '.pdf'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from docx documents and create QuoteModel objects.
        Returns:
            quotes (list): list of QuoteModel objects
        """
        try:
            # Using the '-' argument in order to send the text to the stdout
            # No need to create and delete temporary files
            pipeline = subprocess.Popen(['pdftotext', path, '-'],
                                        stdout=subprocess.PIPE)
            output = pipeline.communicate()
            contents = output[0].decode("utf-8")
            contents = contents.split("\n")
            quotes = []

            for line in contents:
                line = line.split("-")
                if len(line) == 2:
                    body, author = tuple(line)
                    quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(quote)

            return quotes
        except Exception as e:
            print(e)


class CSVIngestor(IngestorInterface):
    """Class definition to import quotes from csv documents."""
    file_extension = '.csv'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from docx documents and create QuoteModel objects.
        Returns:
            quotes (list): list of QuoteModel objects
        """
        try:
            dataframe = read_csv(path)
            content = dataframe.to_dict()
            bodies = content.get("body")
            authors = content.get("author")
            quotes = []

            for index in range(len(bodies)):
                # Insert quote marks to the body
                body = list(bodies.get(index))
                body.insert(0, '"')
                body.append('"')

                quote = QuoteModel(''.join(body), authors.get(index))
                quotes.append(quote)

            return quotes
        except Exception as e:
            print(e)


class Ingestor(IngestorInterface):
    """Load quotes from txt, docx, pdf and csv files and create QuoteModel objects"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from documents and create QuoteModel objects.
        Returns:
            quotes (list): list of QuoteModel objects
        """
        try:
            quotes = []

            if TextIngestor.can_ingest(path):
                quotes = TextIngestor.parse(path)
            elif DocxIngestor.can_ingest(path):
                quotes = DocxIngestor.parse(path)
            elif PDFIngestor.can_ingest(path):
                quotes = PDFIngestor.parse(path)
            elif CSVIngestor.can_ingest(path):
                quotes = CSVIngestor.parse(path)

            return quotes
        except Exception as e:
            print(e)
