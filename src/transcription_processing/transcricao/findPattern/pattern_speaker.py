from .utils import Speech, TransciptionPattern
from typing import List

class TranscriptionParser:

    def __init__(self, raw_text: str):
        self.speeches = []
        self.parse(raw_text)

    def parse(self, raw_text: str) -> List[Speech]:
        self.speeches = list(TransciptionPattern.finditer(raw_text))
        return self.speeches
