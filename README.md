# AI Document Automation Pipeline

A modular Python-based document processing pipeline for extracting text from PDF files, splitting content into manageable chunks, calculating document metrics, and generating structured analysis reports.

This project demonstrates practical Python automation, file processing, JSON-based data handling, and modular pipeline design. It provides a foundation for more advanced document automation and AI integration.

## Project Overview

Business documents often contain information that must be extracted, organized, and prepared for further analysis. This project demonstrates how a repeatable Python workflow can automate several initial document-processing steps.

The pipeline processes a PDF document and generates intermediate files and structured outputs that can be used in subsequent workflows.

### Key Features

- **PDF text extraction:** Extracts text from PDF documents using PyMuPDF.
- **Text chunking:** Splits extracted text into manageable sections for downstream processing.
- **Document metrics:** Calculates basic metrics, including character count and chunk count.
- **Structured JSON output:** Saves analysis results in a machine-readable JSON file.
- **Automated report generation:** Creates a text report based on the generated analysis data.
- **Modular architecture:** Separates extraction, chunking, analysis, reporting, and orchestration into individual Python modules.
- **Reproducible workflow:** Runs the processing steps through a single entry point.

## Pipeline Architecture

```text
PDF Document
     |
     v
Text Extraction
     |
     v
Text Chunking
     |
     v
Document Metrics
     |
     v
JSON Analysis
     |
     v
Text Report
```

The pipeline connects individual processing modules into a repeatable workflow. Intermediate files make the results of each processing stage available for inspection and further development.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and workflow orchestration |
| PyMuPDF | PDF text extraction |
| JSON | Structured analysis output |
| File I/O | Reading source documents and writing results |
| Modular Python functions | Separation of processing responsibilities |

## Project Structure

```text
ai-document-automation/
├── app/
│   ├── pdf_reader.py
│   ├── text_chunker.py
│   ├── document_analyzer.py
│   ├── ai_summarizer.py
│   └── main.py
├── data/
│   └── example_documents/
│       └── test.pdf
├── output/
├── requirements.txt
├── .gitignore
└── README.md
```

### Module Responsibilities

- `pdf_reader.py` — extracts text from the input PDF.
- `text_chunker.py` — divides extracted text into smaller sections.
- `document_analyzer.py` — calculates basic document metrics and writes the results to JSON.
- `ai_summarizer.py` — formats the analysis data into a readable text report.
- `main.py` — coordinates the processing steps and runs the complete pipeline.

## Requirements

- Python 3
- pip

The project dependencies are listed in `requirements.txt`.

## Installation

Clone the repository:

```bash
git clone https://github.com/JuergenVagt/ai-document-automation.git
cd ai-document-automation
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the pipeline from the project root directory:

```bash
python app/main.py
```

The application uses the example PDF configured in `app/main.py`. It extracts the document text, creates text chunks, calculates basic metrics, writes the analysis to JSON, and generates a text report.

For a different input document, update the PDF path in `app/main.py` and ensure that the target file exists.

## Generated Outputs

The pipeline writes its processing results to the `output/` directory.

| Output file | Description |
|---|---|
| `extracted_text.txt` | Text extracted from the PDF |
| `chunks.txt` | Text divided into chunks |
| `analysis.json` | Basic document metrics in JSON format |
| `summary.txt` | Readable text report based on the analysis data |

These files make the processing results inspectable and provide a starting point for additional automation.

## Example Analysis Output

The JSON analysis contains basic document statistics, such as:

```json
{
    "document_length": 566,
    "chunks": 3,
    "characters": 566,
    "status": "analysed"
}
```

The values above are illustrative. Actual results depend on the input text and the pipeline's processing steps.

## Current Scope and Limitations

The current version implements PDF text extraction, text chunking, basic metrics, JSON output, and text report generation.

Despite the module name `ai_summarizer.py`, the current reporting step does not call an external AI model or API. It formats the available analysis data into a text report. The document analysis is based on simple metrics rather than semantic interpretation.

PDFs containing scanned images may require OCR before their text can be processed. The current workflow also uses a configured example input rather than a complete batch-processing interface.

## Potential Extensions

The modular design allows the pipeline to be extended with additional capabilities, including:

- Integration with an AI model for semantic summarization
- OCR for scanned documents
- Batch processing of multiple PDFs
- Extraction of structured information from invoices and business reports
- Export to CSV, Excel, or HTML
- Document classification and metadata extraction
- Validation and error handling for production workflows

These are potential future improvements and are not presented as existing features.

## Professional Applications

The workflow illustrates foundational techniques that can support business automation projects, such as:

- Preparing PDF content for analysis
- Automating repetitive document-processing tasks
- Converting extracted information into structured data
- Creating intermediate outputs for downstream reporting
- Building modular Python workflows that can be extended as requirements evolve

Actual suitability for a business process depends on document quality, input formats, validation requirements, and the accuracy needed for the intended use.

## Project Purpose

This project demonstrates a practical foundation for Python-based document automation. It combines PDF text extraction, text processing, basic analysis, structured output generation, and automated reporting in one modular workflow.

The repository is intended as a portfolio project showing core automation techniques and a clear path toward more advanced document-processing solutions.
