from pdf_reader import extract_text
from text_chunker import save_chunks
from document_analyzer import load_chunks, analyze_document, save_analysis


if __name__ == "__main__":

    pdf_file = "data/example_documents/test.pdf"
    text_file = "output/extracted_text.txt"
    chunks_file = "output/chunks.txt"
    analysis_file = "output/analysis.json"

    print("1/3 PDF wird gelesen...")
    extract_text(pdf_file, text_file)

    print("2/3 Text wird aufgeteilt...")
    save_chunks(text_file, chunks_file)

    print("3/3 Dokument wird analysiert...")
    chunks = load_chunks(chunks_file)
    result = analyze_document(chunks)
    save_analysis(result, analysis_file)

    print("Pipeline erfolgreich abgeschlossen.")