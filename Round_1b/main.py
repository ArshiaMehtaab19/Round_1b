import os
import fitz  # PyMuPDF
import re
import json
from datetime import datetime

# ----------- CONFIGURABLE ----------
persona = "PhD Researcher in Computational Biology"
job_to_be_done = "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"
# -----------------------------------

input_dir = "./input"
output_dir = "./output"
output_filename = "round1b_output.json"

# Step 1: Create a list of keywords from persona + job description
def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    return list(set(words))

keywords = extract_keywords(persona + " " + job_to_be_done)

# Step 2: Score a section's text based on keyword hits
def score_text(text):
    score = 0
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            score += 1
    return score

# Step 3: Process one PDF file
def process_pdf(file_path):
    doc = fitz.open(file_path)
    sections = []
    sub_sections = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if not text or len(text) < 20:
                continue

            # Heuristic: is this a heading?
            is_heading = text.isupper() or re.match(r'^[A-Z][a-z]+\s+[A-Z][a-z]+', text)
            score = score_text(text)

            if score > 0:
                sections.append({
                    "document": os.path.basename(file_path),
                    "page_number": page_num,
                    "section_title": text if is_heading else text[:60] + "...",
                    "importance_score": score
                })
                sub_sections.append({
                    "document": os.path.basename(file_path),
                    "page_number": page_num,
                    "refined_text": text,
                    "importance_score": score
                })

    return sections, sub_sections

# Step 4: Run across all PDFs
def process_all_pdfs():
    all_sections = []
    all_subsections = []
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        full_path = os.path.join(input_dir, pdf_file)
        print(f"📄 Processing: {pdf_file}")
        secs, subs = process_pdf(full_path)
        all_sections.extend(secs)
        all_subsections.extend(subs)

    # Sort results by importance
    sorted_sections = sorted(all_sections, key=lambda x: x["importance_score"], reverse=True)
    sorted_subs = sorted(all_subsections, key=lambda x: x["importance_score"], reverse=True)

    # Final output structure
    output = {
        "metadata": {
            "documents": pdf_files,
            "persona": persona,
            "job_to_be_done": job_to_be_done,
            "timestamp": datetime.now().isoformat()
        },
        "relevant_sections": [
            {
                "document": s["document"],
                "page_number": s["page_number"],
                "section_title": s["section_title"],
                "importance_rank": idx + 1
            }
            for idx, s in enumerate(sorted_sections[:10])
        ],
        "subsection_analysis": [
            {
                "document": s["document"],
                "page_number": s["page_number"],
                "refined_text": s["refined_text"],
                "importance_rank": idx + 1
            }
            for idx, s in enumerate(sorted_subs[:10])
        ]
    }

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, output_filename), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"\n✅ Output saved to: {output_dir}/{output_filename}")

# Entry point
if __name__ == "__main__":
    process_all_pdfs()
