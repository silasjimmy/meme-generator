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


class IngestorInterface(ABC):
    """Ingestor interface class definition."""

    def can_ingest(cls, path: str) -> bool:
        """Can ingest.

        Arguments:
            path (str): path

        Returns:
            bool: can ingest
        """
        pass

    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse.

        Arguments:
            path (str): path

        Returns:
            list: a list of QuoteModel objects
        """
        pass