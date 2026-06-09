ATS Resume Analyzer (AI-Powered Resume Screening System)

==============================================

🚀 Overview

The ATS Resume Analyzer is a Python + Streamlit web application that simulates a real-world Applicant Tracking System (ATS).

It analyzes resumes in PDF format and evaluates candidates based on:

🧠 Skill detection
📊 Weighted ATS scoring system
🧾 Section-based evaluation
💼 Job role prediction
💡 Smart improvement suggestions

👉 This project helps understand how companies automatically filter and rank resumes.

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
✔ Extract text automatically
✔ Detect technical skills
✔ Calculate ATS score (0–100)
✔ Predict job role (AI / Web / Software / Beginner)
✔ Suggest missing skills
✔ Provide improvement tips
✔ Clean Streamlit dashboard UI

🧠 How It Works
📄 PDF Upload
   ↓
🔍 Extract Text (pdfplumber)
   ↓
🧹 Clean Text
   ↓
🧠 Skill Detection
   ↓
📊 ATS Score Calculation
   ↓
💼 Role Prediction
   ↓
💡 Suggestions
   ↓
📺 Display Output
📌 Code Explanation
1️⃣ PDF Text Extraction
def extract_text_from_pdf(pdf_file):

✔ Converts PDF → text
✔ Uses pdfplumber
✔ Makes resume readable for analysis

2️⃣ Text Cleaning
text = re.sub(r'[^a-z0-9\s]', ' ', text)
text = re.sub(r'\s+', ' ', text)

✔ Removes symbols
✔ Normalizes text
✔ Improves matching accuracy

3️⃣ Skill Detection
for skill, weight in SKILL_WEIGHTS.items():

✔ Checks skills in resume
✔ Uses regex matching
✔ Assigns weight to each skill

4️⃣ ATS Score Calculation
final_score = min(score + section_bonus, 100)

✔ Combines:

Skill score
Section bonus

📊 Final range: 0–100

5️⃣ Missing Skills Detection
missing_skills = [s for s in SKILL_WEIGHTS if s not in found_skills]

✔ Shows missing skills
✔ Helps improve resume

6️⃣ Job Role Prediction

✔ Machine Learning → AI Engineer
✔ React / HTML → Frontend Developer
✔ Java / SQL → Software Developer
✔ Else → Beginner

7️⃣ Smart Suggestions

✔ Learn Git & GitHub
✔ Add real-world projects
✔ Learn SQL / React / ML

📊 Example Output
📌 Found Skills: python, java

📊 ATS Score: 58 / 100

⭐ Rating: Intermediate ⭐⭐

💼 Suggested Role: Software Developer

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
🔥 Job matching system

👨‍💻 Conclusion

This project simulates a real ATS system used in companies to:

✔ Filter resumes
✔ Rank candidates
✔ Match job roles

It is a strong beginner-to-intermediate AI project using Python + Streamlit.