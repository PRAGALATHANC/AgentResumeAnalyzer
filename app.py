from flask import Flask, render_template, request
import fitz  # PyMuPDF
from analyze_pdf import analyze_resume_gemini
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        job_description = request.form.get("job_description", "")
        file = request.files.get("resume")
        
        if file and file.filename.endswith(".pdf"):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Extract text and analyze
            resume_content = extract_text_from_pdf(file_path)
            result = analyze_resume_gemini(resume_content, job_description)
    
    return render_template("index.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
