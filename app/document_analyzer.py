import json


def analyze_document(input_file, output_file):

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    analysis = {
        "document_length": len(text),
        "chunks": text.count("CHUNK"),
        "characters": len(text),
        "status": "analysed"
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            analysis,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Dokumentanalyse erfolgreich erstellt.")


if __name__ == "__main__":
    analyze_document(
        "output/chunks.txt",
        "output/analysis.json"
    )