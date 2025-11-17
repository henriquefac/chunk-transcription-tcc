from . import re, dataclass, Speech
from typing import Generator


@dataclass
class TransciptionPattern:
    block_regex: re.Pattern = re.compile(
        r"""
        \[
            (?P<start>\d{2}:\d{2}:\d{2}\.\d+)
            \s*-\s*
            (?P<end>\d{2}:\d{2}:\d{2}\.\d+)
        \]
        \s*
        (?P<speaker>[A-Z0-9_]+):
        \s*
        (?P<text>.*?)
        (?=\n\[|\Z)
        """,
        re.VERBOSE | re.DOTALL,
    )

    @classmethod
    def finditer(cls, raw_text: str) -> Generator[Speech, None, None]:
        for match in cls.block_regex.finditer(raw_text):
            start = match["start"]
            end = match["end"]
            speaker = match["speaker"]
            text = match["text"]

            yield Speech.from_raw(start, end, speaker, text)
