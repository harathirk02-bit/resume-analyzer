ATS Resume Analyzer (AI-Powered Resume Screening System)
🚀 Overview

The ATS Resume Analyzer is a Python + Streamlit web application that simulates a real-world Applicant Tracking System (ATS).

It analyzes resumes in PDF format and evaluates candidates based on:

🧠 Skill detection
📊 Weighted ATS scoring system
🧾 Section-based evaluation
💼 Job role prediction
💡 Smart improvement suggestions

This project helps users understand how real ATS systems filter and rank resumes in companies.

🛠️ Tech Stack
Python 🐍
Streamlit 🌐
pdfplumber 📄
Regex (re module)
🏗️ Project Structure
resume-analyzer/
│
├── app.py                  # Streamlit frontend UI
├── utils/
│   └── analyzer.py        # Backend ATS logic
│
└── README.md
⚙️ Features

✔ Upload resume in PDF format
✔ Extract text automatically from resume
✔ Detect technical skills using NLP (regex-based matching)
✔ Weighted ATS scoring system (0–100)
✔ Section-based bonus scoring
✔ Missing skill detection
✔ Job role prediction (AI / Web / Software / Beginner)
✔ Smart resume improvement suggestions
✔ Clean and interactive Streamlit UI

🧠 How It Works (Workflow)
📄 Upload Resume (PDF)
        ↓
🔍 Extract Text (pdfplumber)
        ↓
🧹 Clean & Normalize Text
        ↓
🧠 Skill Detection (Regex Matching)
        ↓
📊 ATS Score Calculation (Weighted + Bonus)
        ↓
💼 Job Role Prediction
        ↓
💡 Suggestion Engine
        ↓
📺 Display Results in UI
📌 Code Explanation
1️⃣ PDF Text Extraction

📍 File: analyzer.py

def extract_text_from_pdf(pdf_file):

Purpose:

Reads PDF resume page by page
Extracts text using pdfplumber
Converts text into lowercase

✔ This step converts PDF → readable text for processing.

2️⃣ Text Cleaning
text = re.sub(r'[^a-z0-9\s]', ' ', text)
text = re.sub(r'\s+', ' ', text)

Purpose:

Removes special characters
Removes extra spaces
Normalizes text for accurate matching
3️⃣ Skill Detection System
for skill, weight in SKILL_WEIGHTS.items():
    if re.search(r'\b' + re.escape(skill) + r'\b', text):

How it works:

Matches skills inside resume text
Uses regex word boundaries for accuracy
Assigns weight to each skill

Example:

Skill	Weight
Python	10
Java	8
React	10
4️⃣ ATS Score Calculation
final_score = min(score + section_bonus, 100)

Components:

Skill-based score
Section bonuses:
Skills
Projects
Experience
Education
Certifications

📊 Score Range: 0 → 100

5️⃣ Missing Skills Detection
missing_skills = [s for s in SKILL_WEIGHTS if s not in found_skills]

Purpose:

Identifies missing technical skills
Helps users improve resumes
6️⃣ Job Role Prediction

Based on detected skills:

🧠 Machine Learning / NLP → AI / Data Scientist
🌐 HTML / CSS / React → Frontend / Full Stack Developer
💻 Java / C / SQL → Software Developer
📌 Otherwise → Beginner / Fresher
7️⃣ Smart Suggestions Engine

Example suggestions:

Learn Git & GitHub
Add real-world projects
Learn SQL / React / Machine Learning
Focus on one tech stack

Purpose:

Gives personalized resume improvement tips
Helps increase ATS score
8️⃣ Streamlit UI (Frontend)

📍 File: app.py

Responsibilities:

Upload resume PDF
Display extracted text
Show results:
Found skills
Missing skills
ATS score
Rating
Suggested role
Improvement suggestions
📊 Example Output
📌 Found Skills:
python, java

📊 ATS Score:
58 / 100

⭐ Rating:
Intermediate ⭐⭐

💼 Suggested Role:
Software Developer

💡 Suggestions:
👉 Learn Git & GitHub  
👉 Add real-world projects  
👉 Learn SQL  
📦 Installation
pip install streamlit pdfplumber
▶️ Run Project
streamlit run app.py
🚀 Future Enhancements

🔥 OCR support for scanned resumes
🔥 AI-based semantic skill detection
🔥 Resume PDF report download
🔥 Graph-based skill visualization
🔥 Job matching system like LinkedIn/Naukri
🔥 AI Chat-based resume reviewer

👨‍💻 Conclusion

This project simulates a real-world ATS system used in companies to:

Filter candidates
Rank resumes
Match job roles

It is a strong beginner-to-intermediate AI project covering:

✔ Resume screening
✔ NLP basics
✔ Streamlit applications
✔ Python backend logic
✔ Real-world ATS simulation