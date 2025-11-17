from src.transcricao.findPattern import TranscriptionParser
from configPy import Config

file_teste = next(Config.get_dir_files().iter_files())

with open(file_teste, "r") as file:
    text = file.read()

transcription = TranscriptionParser(text)

for speech in transcription.speeches:
    print(speech.get_text_chunks())
