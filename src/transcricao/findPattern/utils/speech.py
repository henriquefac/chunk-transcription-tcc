from . import dataclass
from datetime import timedelta
import hashlib
from .chunk_text import List, chunk_speech_text

def timestamp_to_delta(ts: str) -> timedelta:
    h, m, s = ts.split(":")
    seconds = float(s)
    return timedelta(hours=int(h), minutes=int(m), seconds=seconds)

@dataclass
class TextChunk:
    time_start: timedelta
    time_end: timedelta
    speaker: str
    text: str
    speech_id: str

    @classmethod
    def from_speech(cls, speech: "Speech", text: str) -> "TextChunk":
        """
        Cria um chunk diretamente a partir de um objeto Speech.
        """
        return cls(
            time_start=speech.time_start,
            time_end=speech.time_end,
            speaker=speech.speaker,
            text=text,
            speech_id=speech.speech_id,
        )


@dataclass
class Speech:
    time_start: timedelta
    time_end: timedelta
    speaker: str
    text: str
    speech_id: str

    # -----------------------------
    # Class constructors
    # -----------------------------
    @classmethod
    def compute_speech_id(cls, text: str) -> str:
        """
        Gera um hash único baseado exclusivamente no texto da fala.
        """
        h = hashlib.sha1(text.strip().encode("utf-8")).hexdigest()
        return h[:12]

    @classmethod
    def from_raw(cls, time_start_raw: str, time_end_raw: str,
                 speaker: str, text: str) -> "Speech":
        """
        Cria um Speech a partir de dados brutos da transcrição.
        """
        text_clean = text.strip()

        return cls(
            time_start=timestamp_to_delta(time_start_raw),
            time_end=timestamp_to_delta(time_end_raw),
            speaker=speaker.strip(),
            text=text_clean,
            speech_id=cls.compute_speech_id(text_clean),
        )

    # -----------------------------
    # Chunking
    # -----------------------------
    def get_text_chunks(self, max_chars: int | None = None,
                        overlap_words: int = 0) -> List[TextChunk]:
        """
        Divide o texto da fala em chunks e retorna TextChunks completos,
        preservando metadados da fala original.
        """
        chunks = chunk_speech_text(
            self.text,
            max_chars=max_chars or 500,
            overlap_words=overlap_words,
        )

        return [TextChunk.from_speech(self, ch) for ch in chunks]

    # -----------------------------
    # Debug
    # -----------------------------
    def __str__(self):
        return (
            f"\n[{self.time_start} - {self.time_end}] {self.speaker}\n"
            f"ID da fala: {self.speech_id}\n"
            f"Tamanho da fala: {len(self.text)}\n\n"
            f"FALA: {self.text[:60]}...\n"
        )
