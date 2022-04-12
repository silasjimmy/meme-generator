""""""


class QuoteModel:
    """A class definition to instantiate quote objects"""

    def __init__(self, body: str, author: str) -> None:
        """Initialize a quote object with the quote's body and author.

        Arguments:
            body (str): The body of the quote
            author (str): The author of the quote
        """
        self.body = body
        self.author = author