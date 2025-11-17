from typing import List

def chunk_speech_text(
    text: str,
    max_chars: int = 500,
    overlap_words: int = 3,
)-> List[str]:
    """
    Divide o texto em chunks respeitando:
      - cálculo proporcional de chunk_len
      - divisão por palavras
      - overlap de N palavras
    """

    text = text.strip()
    n = len(text)

    # Se não ultrapassa limite → não chunkar
    if n <= max_chars:
        return [text]

    # -----------------------------
    # 1) Cálculo proporcional (sua lógica)
    # -----------------------------
    int_division = n // max_chars
    rest_division = n % max_chars

    if int_division == 1:
        chunk_len = n // 2
    elif rest_division == 0:
        chunk_len = n // int_division
    else:
        chunk_len = n // (int_division - 1)

    # -----------------------------
    # 2) Chunking baseado em palavras
    # -----------------------------
    words = text.split()
    chunks = []
    current_words = []

    for word in words:
        new_text = " ".join(current_words + [word])

        if len(new_text) > chunk_len:
            # fecha chunk atual
            chunks.append(" ".join(current_words))

            # aplica overlap
            if overlap_words > 0:
                current_words = current_words[-overlap_words:]
            else:
                current_words = []

        current_words.append(word)

    # último chunk
    if current_words:
        chunks.append(" ".join(current_words))

    return chunks


