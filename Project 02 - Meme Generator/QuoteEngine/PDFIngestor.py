"""PDF Ingestor."""

import os
import random
import subprocess
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingests a pdf file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file with the PDFIngestor.

        Arguments:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: A list of the QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can\'t ingest path')

        quotes = []
        tmp = f"./tmp/{random.randint(0, 1000)}.txt"

        try:
            subprocess.call(['pdftotext', path, tmp])
            with open(tmp, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError as e:
            print(f'Error: {e}')
        else:
            for line in lines:
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    split = line.split(' - ')
                    quotes.append(QuoteModel(split[0], split[1]))

        if os.path.exists(tmp):
            os.remove(tmp)

        return quotes