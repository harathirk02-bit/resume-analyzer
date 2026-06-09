ATS Resume Analyzer (AI-Powered Resume Screening System)
🚀 Overview

The ATS Resume Analyzer is a Python + Streamlit web application that simulates a real Applicant Tracking System (ATS) used in companies.

It automatically analyzes PDF resumes and evaluates candidates based on skills, experience, and overall profile quality.

👉 It helps users understand how companies filter, rank, and shortlist resumes automatically.

🛠️ Tech Stack
🐍 Python (Core Logic)
🌐 Streamlit (Frontend UI)
📄 pdfplumber (PDF Text Extraction)
🔍 Regex (Skill Detection & Text Processing)
🏗️ Project Structure

The project has two main parts:

app.py → Streamlit frontend (UI, file upload, result display)
utils/analyzer.py → Backend logic (resume analysis, scoring, predictions)
⚙️ Features

✔ Upload resume in PDF format
✔ Extract text automatically from resume
✔ Detect technical skills using pattern matching
✔ Calculate ATS score (0–100)
✔ Predict job role (AI / Web / Software / Beginner)
✔ Identify missing skills
✔ Provide smart improvement suggestions
✔ Clean and simple user interface

🧠 How It Works

The system follows this workflow:

User uploads a PDF resume
Text is extracted from the PDF
Text is cleaned and normalized
Skills are detected using predefined keywords
ATS score is calculated using weighted logic
Job role is predicted based on skills
Suggestions are generated
Results are displayed in UI
📌 Code Logic Explanation

The resume is first converted from PDF into plain text so it can be processed.

Then the text is cleaned by removing special characters, symbols, and extra spaces to improve accuracy.

Skill detection is performed by matching predefined technical keywords in the resume.

The ATS score is calculated using skill weights and additional bonus marks from important sections like skills, projects, experience, and certifications.

Missing skills are identified by comparing detected skills with the full skill list.

Job role prediction is done based on skill categories such as AI/ML, web development, or software development.

Finally, the system generates personalized suggestions to improve resume quality.

📊 Output

The system displays:

Detected skills
ATS score (0–100)
Rating (Beginner / Intermediate / Advanced)
Suggested job role
Improvement suggestions
📦 Installation

Install required dependencies:

streamlit
pdfplumber
▶️ Run Project

Run the application using Streamlit:

The app will open in the browser where you can upload resumes and see results instantly.

🚀 Future Enhancements
OCR support for scanned resumes
AI-based semantic skill detection
Resume PDF download report
Graph-based skill visualization
Job matching system like LinkedIn/Naukri
👨‍💻 Conclusion

This project simulates a real ATS system used in companies.

It helps in:
✔ Resume filtering
✔ Candidate ranking
✔ Job role matching

👉 It is a strong AI + Python beginner project for learning and portfolio use.

⭐ DONE
