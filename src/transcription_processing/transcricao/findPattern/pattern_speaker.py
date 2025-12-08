from .utils import Speech, TransciptionPattern
from typing import List

class TranscriptionParser:

    def __init__(self, raw_text: str):
        self.speeches = []
        self.parse(raw_text)

    def parse(self, raw_text: str) -> List[Speech]:
        self.speeches = list(TransciptionPattern.finditer(raw_text))
        return self.speeches
    
    # criar função para construir chunls a partir da transcrição
    def get_chunks_text(self, thrashold: int = 5000):
        all_speeches = [speech.get_speech_format() for speech in self.speeches]

        chunks = []
        this_chunk = ""
        this_chunk_len = 0

        for (speech, lenspch) in all_speeches:
            this_chunk += speech + "\n\n"
            this_chunk_len += lenspch

            if this_chunk_len >= thrashold:
                chunks.append(this_chunk)
                this_chunk = ""
                this_chunk_len = 0
        
        return chunks
