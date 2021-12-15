"""Quote Model Object."""

class QuoteModel():
    """The quote model object."""

    def __init__(self, body, author):
        """Set up a quote model object.

        Arguments:
            body (str): Body of quote.
            author (str): Author of quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of the QuoteModel object in a human-readable format.

        Returns:
            str: human-readable QuoteModel representation.
        """
        return f'{self.body} - {self.author}'
