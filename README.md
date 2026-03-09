🤖 Agentic Resume AnalyzerAn AI-powered application that leverages Google Gemini 1.5 Flash to perform deep semantic analysis of resumes against specific job descriptions. This tool provides more than just keyword matching—it offers professional insights into candidate compatibility and actionable growth suggestions.🌟 Key FeaturesPDF Text Extraction: Uses PyMuPDF (fitz) to seamlessly extract raw text from uploaded PDF resumes.AI-Driven Match Scoring: Calculates a compatibility score out of 100 using advanced NLP.Gap Analysis: Automatically highlights specific missing skills or experiences based on the job requirements.Resume Optimization: Provides structured suggestions to improve the resume's alignment with the target role.Modern Web UI: Features a responsive, gradient-styled interface built with Flask and custom CSS.🛠️ Tech StackComponentTechnologyBackendPython & Flask Generative AIGoogle Gemini 1.5 Flash PDF EnginePyMuPDF (fitz) StylingCSS3 (Linear Gradients & Flexbox) Environmentpython-dotenv 🗂️ Project StructurePlaintextAgentResumeAnalyzer/
├── app.py              # Flask server, file handling, and PDF parsing 
├── analyze_pdf.py      # Gemini AI configuration and prompt engineering 
├── templates/
│   └── index.html      # Frontend HTML structure with Jinja2 templates [cite: 2]
├── static/
│   └── style.css       # Custom UI design and styling 
├── uploads/            # Temporary storage for uploaded PDF files 
└── .env                # Environment variables for API security 
🚀 Getting Started1. PrerequisitesPython 3.xA Google Gemini API Key 2. Environment ConfigurationCreate a .env file in the root directory and add your API key:BashGEMINI_APP_KEY=your_actual_api_key_here
3. InstallationInstall the required dependencies via pip:Bashpip install flask pymupdf google-generativeai python-dotenv
4. Run the ApplicationStart the Flask server:Bashpython app.py
Open your browser and navigate to http://127.0.0.1:5000.🧠 AI Logic & ConfigurationThe application uses the gemini-1.5-flash model with specific configurations to ensure high-quality analysis:Temperature: 1.0 (allows for creative and insightful suggestions).Top P: 0.95.Prompt Architecture: The model is instructed to act as a "professional resume analyzer" and return a structured response including Match Score, Missing Skills, Suggestions, and a Summary.
