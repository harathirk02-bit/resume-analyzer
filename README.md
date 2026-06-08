# AI Resume Analyzer

## Overview

AI Resume Analyzer is a web application developed using Python and Streamlit that helps users evaluate their resumes automatically. The system extracts text from PDF resumes, identifies technical skills, calculates a resume score, generates a rating, and suggests missing skills that can improve employability.

The project demonstrates the use of Python programming, PDF processing, text analysis, and web application development in a simple and practical manner.

---

## Features

### Resume Upload

Users can upload their resumes in PDF format through an easy-to-use web interface.

### Text Extraction

The application extracts text from uploaded PDF resumes using the PyPDF2 library.

### Skill Detection

The extracted text is compared with a predefined list of technical skills such as Python, Java, SQL, React, Machine Learning, and others.

### Resume Score Calculation

A score is generated based on the number of matching skills detected in the resume.

### Resume Rating

The system categorizes resumes into:

* Beginner
* Intermediate
* Advanced

### Skill Recommendations

Missing skills are displayed to help users improve their resumes.

---

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* Streamlit
* PyPDF2
* Pandas

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```text
resume-analyzer/
│
├── app.py
├── requirements.txt
│
└── utils/
    ├── __init__.py
    └── analyzer.py
```

---

## File Description

### app.py

The main application file.

Responsibilities:

* Creates the Streamlit user interface
* Accepts PDF uploads
* Calls analysis functions
* Displays scores, ratings, and recommendations
* Shows detected and missing skills

### analyzer.py

Contains the backend logic.

Responsibilities:

* Extract text from PDF resumes
* Detect technical skills
* Calculate resume score
* Generate ratings
* Identify missing skills

### requirements.txt

Contains all required project dependencies.

Example:

```text
streamlit
PyPDF2
pandas
```

---

## System Workflow

### Step 1

User uploads a PDF resume.

### Step 2

The application extracts text from the uploaded file.

### Step 3

The extracted text is converted into lowercase format.

### Step 4

The system compares resume content with predefined technical skills.

### Step 5

Matched skills are stored as detected skills.

### Step 6

Unmatched skills are identified as missing skills.

### Step 7

The resume score is calculated.

### Step 8

A rating is assigned based on the score.

### Step 9

Results are displayed on the Streamlit dashboard.

---

## Code Explanation

### Text Extraction Function

Purpose:

* Read PDF files
* Extract text from every page

Working:

1. Open uploaded PDF
2. Read each page
3. Extract text
4. Return combined text

---

### Skill Detection Function

Purpose:

* Find technical skills present in the resume

Working:

1. Load predefined skill list
2. Compare each skill with extracted text
3. Store matched skills
4. Generate detected skills list

---

### Score Calculation Logic

Formula:

Resume Score = (Detected Skills / Total Skills) × 100

Example:

Total Skills = 12

Detected Skills = 9

Score = (9 ÷ 12) × 100

Score = 75%

---

### Rating Logic

| Score Range | Rating       |
| ----------- | ------------ |
| 0 – 49      | Beginner     |
| 50 – 79     | Intermediate |
| 80 – 100    | Advanced     |

---

## Sample Output

### Skills Detected

* Python
* SQL
* React
* Git

### Missing Skills

* FastAPI
* Flask
* Machine Learning

### Resume Score

75%

### Resume Rating

Intermediate

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/harathirk02-bit/resume-analyzer.git
```

### Move into Project Folder

```bash
cd resume-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Email Extraction
* Phone Number Extraction
* Resume Download Report
* AI-Based Suggestions
* Job Role Recommendation
* Better UI Design
* Cloud Deployment

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Python Programming
* Streamlit Development
* PDF Processing
* Text Analysis
* Git and GitHub
* Resume Evaluation Techniques
* Full Stack Application Basics

---

## Author

Harathi

B.Tech CSE (AI & ML)

JNTUA
