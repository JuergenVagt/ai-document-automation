import fitz
from pathlib import Path


def extract_text(pdf_path, output_path):
    document = fitz.open(pdf_path)

    full_text = ""

    for page in document:
        full_text += page.get_text()

    Path(output_path).write_text(
        full_text,
        encoding="utf-8"
    )

    print("Text erfolgreich extrahiert.")


if __name__ == "__main__":
    input_pdf = "data/example_documents/test.pdf"
    output_txt = "output/extracted_text.txt"

    extract_text(input_pdf, output_txt)