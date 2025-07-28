Round 1B – Persona-Driven Document Intelligence
Repository Name: PersonaDrivenDocInsights

Project Overview
This solution extracts and ranks document content based on user personas (e.g., job seekers, students) using keyword-based relevance scoring. It builds on heading detection (Round 1A) and prioritizes information matching persona needs.

Features
Persona-specific content filtering

Dynamic keyword-based scoring system

Prioritized structured output based on role

Multilingual document support

Technologies Used
Python

Tesseract OCR

Langdetect

Custom keyword relevance scoring

Input/Output
Input: JSON files with heading-content pairs (from Round 1A)

Output: Prioritized JSON with top relevant sections

📦 Run using Docker
bash
Copy
Edit
docker build -t personadocinsights .
docker run --rm -v "$PWD/input:/app/input" -v "$PWD/output:/app/output" personadocinsights
