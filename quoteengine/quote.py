"""This module creates QuoteModel objects from quotes with a body and author."""


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
        return f"{self.body} - {self.author}"
