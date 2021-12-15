"""Text Ingestor."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingests a txt file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file with the TextIngestor.

        Arguments:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: A list of the QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can\'t ingest path')

        quotes = []
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    split = line.split(' - ')
                    quotes.append(QuoteModel(split[0], split[1]))

        return quotes