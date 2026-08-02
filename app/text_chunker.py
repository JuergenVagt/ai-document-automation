def chunk_text(text, chunk_size=500):
    """
    Teilt einen langen Text in kleinere Abschnitte.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def save_chunks(chunks, output_file):
    """
    Speichert die Text-Chunks in einer Datei.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        for index, chunk in enumerate(chunks):
            file.write(f"\n--- CHUNK {index + 1} ---\n")
            file.write(chunk)
            file.write("\n")


if __name__ == "__main__":

    input_file = "output/extracted_text.txt"
    output_file = "output/chunks.txt"

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = chunk_text(text)

    save_chunks(chunks, output_file)

    print(f"{len(chunks)} Text-Chunks erstellt.")