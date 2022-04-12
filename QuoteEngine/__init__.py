""""""

from abc import ABC
from typing import List


class QuoteModel:
    """A class definition to instantiate quote objects."""

    def __init__(self, body: str, author: str) -> None:
        """Initialize a quote object with the quote's body and author.

        Arguments:
            body (str): The body of the quote
            author (str): The author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Returns:
            str: string representation of the object
        """
        return f"\"{self.body}\" - {self.author}"


class IngestorInterface(ABC):
    """Ingestor interface class definition."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Can ingest.

        Arguments:
            path (str): path

        Returns:
            bool: can ingest
        """
        return True

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse.

        Arguments:
            path (str): path

        Returns:
            list: a list of QuoteModel objects
        """
        return []


class CSVImporter(IngestorInterface):
    """Class definition to import quotes from csv documents."""
    pass


class DocxImporter(IngestorInterface):
    """Class definition to import quotes from docx documents."""
    pass


class PDFImporter(IngestorInterface):
    """Class definition to import quotes from pdf documents."""
    pass


class TextImporter(IngestorInterface):
    """Class definition to import quotes from text documents."""
    pass


class Ingestor(IngestorInterface):
    """"""
    pass