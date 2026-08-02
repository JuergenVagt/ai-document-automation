from pdf_reader import extract_text
from text_chunker import save_chunks
from document_analyzer import analyze_document
from ai_summarizer import create_summary


input_pdf = "data/example_documents/test.pdf"

text_file = "output/extracted_text.txt"
chunks_file = "output/chunks.txt"
analysis_file = "output/analysis.json"
summary_file = "output/summary.txt"


print("1/4 PDF wird gelesen...")
extract_text(input_pdf, text_file)


print("2/4 Text wird aufgeteilt...")
save_chunks(text_file, chunks_file)


print("3/4 Dokument wird analysiert...")
analyze_document(chunks_file, analysis_file)


print("4/4 KI-Zusammenfassung wird erstellt...")
create_summary(analysis_file, summary_file)


print("Komplette KI-Dokumentenpipeline abgeschlossen.")