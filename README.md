ATS Resume Analyzer (AI-Powered Resume Screening System)
🚀 Overview

The ATS Resume Analyzer is a Python + Streamlit application that simulates a real ATS system.

It analyzes resumes and evaluates candidates based on:

Skill detection
ATS scoring
Job role prediction
Suggestions
🛠️ Tech Stack
Python
Streamlit
pdfplumber
Regex
🏗️ Project Structure
app.py → Frontend UI
utils/analyzer.py → Backend logic
⚙️ Features
Upload PDF resume
Extract text automatically
Detect skills
Generate ATS score
Predict job role
Suggest improvements
🧠 How It Works
Upload resume
Extract text
Clean text
Detect skills
Calculate score
Predict role
Show results
📌 Code Logic
📄 PDF Extraction

Converts PDF into text.

🧹 Cleaning

Removes symbols and noise.

🧠 Skill Detection

Finds matching skills from resume.

📊 Scoring

Calculates ATS score out of 100.

💼 Role Prediction

Suggests job role based on skills.

📊 Output
Skills found
ATS score
Rating
Suggested role
Suggestions
🚀 Run Project
streamlit run app.py