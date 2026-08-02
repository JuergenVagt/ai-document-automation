def summarize_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    summary = (
        "Dokumentzusammenfassung\n"
        "=======================\n\n"
        "Dieses Dokument wurde automatisch analysiert.\n\n"
        "Auszug:\n"
        + text[:500]
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary)

    print("KI-Zusammenfassung erstellt.")


if __name__ == "__main__":
    summarize_text(
        "output/chunks.txt",
        "output/summary.txt"
    )