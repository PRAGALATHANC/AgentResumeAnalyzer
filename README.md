# 🤖 Agentic Resume Analyzer

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini_1.5_Flash-purple?style=flat-square&logo=google-gemini)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

An AI-powered application that leverages **Google Gemini 1.5 Flash** to perform deep semantic analysis of resumes against specific job descriptions. This tool moves beyond simple keyword matching to offer professional insights into candidate compatibility and actionable growth suggestions.

---

## 📖 Overview

This service provides an intelligent interface for recruiters and job seekers to evaluate resume strength. [cite_start]It extracts text from PDF documents  [cite_start]and uses advanced Large Language Models (LLMs) to provide a structured breakdown of a candidate's fit for a specific role.

### Key Features
* [cite_start]📄 **PDF Text Extraction:** Uses `PyMuPDF` (fitz) to seamlessly extract raw text from uploaded PDF resumes.
* [cite_start]🎯 **AI-Driven Match Scoring:** Calculates a compatibility score out of 100 using advanced NLP.
* [cite_start]🔍 **Gap Analysis:** Automatically highlights specific missing skills or experiences based on the job requirements.
* [cite_start]💡 **Resume Optimization:** Provides structured suggestions to improve the resume's alignment with the target role.
* [cite_start]🎨 **Modern Web UI:** Features a responsive, gradient-styled interface built with Flask and custom CSS[cite: 1, 2].

---

## 🏗️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | [cite_start]Python, Flask  |
| **Generative AI** | [cite_start]Google Gemini 1.5 Flash  |
| **PDF Engine** | [cite_start]PyMuPDF (fitz)  |
| **Styling** | [cite_start]CSS3 (Linear Gradients & Flexbox) [cite: 1] |
| [cite_start]**Environment** | python-dotenv  |

---

## 🗂️ Project Structure

```text
AgentResumeAnalyzer/
├── app.py              # Flask server, file handling, and PDF parsing 
├── analyze_pdf.py      # Gemini AI configuration and prompt engineering [cite: 4, 6]
├── templates/
│   └── index.html      # Frontend HTML structure with Jinja2 templates [cite: 2]
├── static/
│   └── style.css       # Custom UI design and styling [cite: 1]
├── uploads/            # Temporary storage for uploaded PDF files 
└── .env                # Environment variables for API security
