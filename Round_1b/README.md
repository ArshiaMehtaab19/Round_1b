 Persona-Driven Document Intelligence – Round 1B Submission
**Problem Statement
This project is built for Round 1B of the Adobe GenAI Hackathon under the theme “Connect What Matters — For the User Who Matters.”
We were asked to design a document intelligence system that can extract and prioritize the most relevant sections from a collection of PDFs, based on a given persona and their job-to-be-done.

**Solution Overview
Our system performs intelligent document analysis in a generic, extensible way to adapt to various document types, personas, and use cases. It uses lightweight OCR and NLP-based techniques to extract meaningful headings, sub-sections, and relevant context from input PDFs.

We handle multiple languages (like English, Hindi, and Telugu) using OCR capabilities. The extracted sections are ranked by importance, and refined outputs are structured into a well-formatted JSON.

**How It Works
Input:

Folder of 3–10 related PDFs

JSON defining:

Persona (e.g., Researcher, Student, Analyst)

Job to be done (e.g., Summarize financials, Study specific topics)

Processing:

PDFs are parsed using OCR (via PyMuPDF + Tesseract)

Headings are detected using layout patterns and font statistics

Relevant sections are ranked based on semantic relevance to the persona’s task

Final structured output is saved as output.json

Output:

Contains:

Metadata (documents, persona, job, timestamp)

Extracted Sections with heading, page number, rank

Refined sub-section analysis with contextual summaries

**Tech Stack
Python

PyMuPDF

Tesseract OCR (multilingual)

scikit-learn

Regular expressions

Docker (for containerized execution)

.
├── input/                   # Folder for input PDF documents
├── output/                  # Final output JSON will be saved here
├── main.py                  # Code execution script
├── Dockerfile               # Build configuration
└── methodology.md           # Methodology document

**Output Format
Check round1b_output.json for output.


