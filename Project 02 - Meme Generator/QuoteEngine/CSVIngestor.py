"""CSV File Ingestor."""

from typing import List
import pandas as pd
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingests a csv file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file with the CSVIngestor.

        Arguments:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: A list of the QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can\'t ingest path')

        quotes = []
        df = pd.read_csv(path, header=0)
        for col, row in df.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))

        return quotes