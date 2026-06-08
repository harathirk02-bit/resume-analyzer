from PyPDF2 import PdfReader

SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "fastapi",
    "flask",
    "mysql"
]


def extract_text(uploaded_file):
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text.lower()


def analyze_resume(text):

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    missing_skills = [
        skill for skill in SKILLS
        if skill not in found_skills
    ]

    score = int((len(found_skills) / len(SKILLS)) * 100)

    if score >= 80:
        rating = "Advanced"
    elif score >= 50:
        rating = "Intermediate"
    else:
        rating = "Beginner"

    return found_skills, missing_skills, score, rating