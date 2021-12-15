"""Docx File Ingestor."""

import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingests a docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file with the DocxIngestor.

        Arguments:
            path (str): Path to the file.

        Returns:
            List[QuoteModel]: A list of the QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Can\'t ingest path')

        quotes = []
        docx_file = docx.Document(path)
        for paragraph in docx_file.paragraphs:
            if paragraph.text != "":
                split = paragraph.text.split(' - ')
                quotes.append(QuoteModel(split[0], split[1]))

        return quotes