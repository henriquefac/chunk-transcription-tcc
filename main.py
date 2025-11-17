from configPy import Config
import re

files_dir = Config.get_dir_files()

file_teste = next(files_dir.iter_files())

# Padrão
# [00:00:00.00 - 00:00:00.00] SPEAKER
text = "[00:00:14.965 - 00:00:16.011] SPEAKER_02: de Atenção Divina"

pattern = re.compile(
    r"\[(\d{2}:\d{2}:\d{2}\.\d{3})\s*-\s*(\d{2}:\d{2}:\d{2}\.\d{3})\]\s*([A-Za-z0-9_]+):"
)

m = pattern.search(text)


print(re.findall(pattern, text))
print("Start:", m.group(1))
print("End:", m.group(2))
print("Speaker:", m.group(3))
