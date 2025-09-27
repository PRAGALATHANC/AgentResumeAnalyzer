import google.generativeai as genai
import os

# Configure Gemini API
api_key = os.getenv("GEMINI_APP_KEY")

# If .env not used, fallback to hardcoded key
if not api_key:
    api_key = "AIzaSyDR0oSYZqDKOPnj9OgC41HZnu-5iLyNIps"

genai.configure(api_key=api_key)

# Model configuration
configuration = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "stop_sequences": []
}

# Model initialization
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=configuration
)

# Function to analyze resume
def analyze_resume_gemini(resume_content, job_description):
    prompt = f"""
    You are a professional resume analyzer.

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    - Give a match score out of 100.
    - Highlight missing skills or experiences.
    - Suggest improvements.

    Return the result in structured format:
    Match Score: XX/100
    Missing Skills:
    - ...
    Suggestions:
    - ...
    Summary:
    ...
    """
    response = model.generate_content([prompt])
    return response.text
