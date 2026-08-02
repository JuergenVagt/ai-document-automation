import json


def create_summary(analysis_file, output_file):
    with open(analysis_file, "r", encoding="utf-8") as file:
        analysis = json.load(file)

    summary = f"""
Dokumentenzusammenfassung

Anzahl Chunks: {analysis.get("chunks", "unbekannt")}

Analyse:
{analysis}
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary)

    print("KI-Zusammenfassung erstellt.")


if __name__ == "__main__":
    create_summary(
        "output/analysis.json",
        "output/summary.txt"
    )