ATS Resume Analyzer (Python + Streamlit)
🚀 Overview

The ATS Resume Analyzer is a Python-based web application that simulates an Applicant Tracking System (ATS).

It analyzes resumes in PDF format and evaluates them based on:

🧠 Skills detection
📊 Weighted scoring system
🧾 Section-based bonus scoring
💼 Job role prediction
💡 Smart improvement suggestions
🛠️ Tech Stack
Python 🐍
Streamlit 🌐
pdfplumber 📄
Regex (re module)
🏗️ Project Structure
resume-analyzer/
│
├── app.py                  # Streamlit UI (Frontend)
│
├── utils/
│   └── analyzer.py        # ATS logic (Backend engine)
│
└── README.md
⚙️ Features
✔ Upload resume in PDF format
✔ Extract text automatically
✔ Detect technical skills
✔ Calculate ATS score (0–100)
✔ Predict job role (AI / Web / Software / Beginner)
✔ Suggest missing skills
✔ Provide improvement tips
✔ Clean Streamlit dashboard UI
🧠 How It Works (Workflow)
📄 PDF Resume Upload
        ↓
🔍 Extract Text (pdfplumber)
        ↓
🧹 Clean Text (remove symbols, normalize)
        ↓
🧠 Skill Detection (regex matching)
        ↓
📊 Score Calculation (weighted scoring + bonus)
        ↓
💼 Job Role Prediction
        ↓
💡 Smart Suggestions
        ↓
📺 Display Results in Streamlit UI
📌 Code Explanation
1️⃣ PDF Text Extraction

📍 File: analyzer.py

Function:

def extract_text_from_pdf(pdf_file):

Purpose:

Reads uploaded PDF resume
Extracts text from each page using pdfplumber
Converts text to lowercase

Why it matters:
ATS systems cannot directly analyze PDFs — they must convert them into text first.

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

Skill score (based on detected skills)
Section bonus:
Skills
Projects
Experience
Education
Certifications

Range: 0 → 100

5️⃣ Missing Skills Detection
missing_skills = [s for s in SKILL_WEIGHTS if s not in found_skills]

Purpose:

Lists skills not present in resume
Helps users improve their profile
6️⃣ Job Role Prediction

Based on skills detected:

🧠 Machine Learning / NLP → Data Science / AI Engineer
🌐 React / HTML / CSS → Frontend / Full Stack Developer
💻 Java / C / SQL → Software Developer
📌 Else → Beginner / Fresher
7️⃣ Smart Suggestions Engine

Example:

Learn Git & GitHub
Add real-world projects
Learn SQL / React / ML basics

Purpose:

Gives personalized resume improvement tips
Helps increase ATS score
8️⃣ Streamlit UI (Frontend)

📍 File: app.py

Responsibilities:

Upload resume PDF
Show extracted text
Display results:
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
👨‍💻 Conclusion

This project simulates a real-world ATS system used in companies to:

Filter candidates
Rank resumes
Match job roles

It is a great beginner-to-intermediate AI project for:

✔ Resume screening
✔ NLP basics
✔ Streamlit applications
✔ Python backend logic