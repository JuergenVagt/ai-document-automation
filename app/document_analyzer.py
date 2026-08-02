import json


def analyze_document(chunks):
    """
    Analysiert Text-Chunks.
    Später wird hier ein KI-Modell angeschlossen.
    """

    full_text = "\n".join(chunks)

    analysis = {
        "document_length": len(full_text),
        "number_of_chunks": len(chunks),
        "summary": "Automatische Zusammenfassung wird hier später erzeugt.",
        "keywords": [
            "Dokument",
            "Analyse",
            "KI"
        ]
    }

    return analysis


def load_chunks(input_file):
    """
    Liest die erzeugten Text-Chunks ein.
    """

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = text.split("--- CHUNK")

    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]


def save_analysis(data, output_file):
    """
    Speichert Analyse als JSON.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


if __name__ == "__main__":

    input_file = "output/chunks.txt"
    output_file = "output/analysis.json"

    chunks = load_chunks(input_file)

    result = analyze_document(chunks)

    save_analysis(result, output_file)

    print("Dokumentanalyse erfolgreich erstellt.")