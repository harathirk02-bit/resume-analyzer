import pdfplumber
import re

# ---------------- SKILL DATABASE ----------------
SKILL_WEIGHTS = {
    "python": 10,
    "java": 8,
    "c": 5,
    "c++": 6,
    "sql": 8,
    "mysql": 6,
    "html": 4,
    "css": 4,
    "javascript": 9,
    "react": 10,
    "reactjs": 10,
    "git": 5,
    "github": 5,
    "fastapi": 10,
    "flask": 8,
    "machine learning": 12,
    "artificial intelligence": 12,
    "nlp": 10,
    "pandas": 8,
    "numpy": 8,
    "streamlit": 9
}

# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except:
        return ""

    return text.lower()

# ---------------- RESUME ANALYSIS ----------------
def analyze_resume(text):

    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    found_skills = []
    score = 0

    # Skill detection
    for skill, weight in SKILL_WEIGHTS.items():
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)
            score += weight

    found_skills = list(set(found_skills))

    # Section bonus
    sections = {
        "skills": 5,
        "technical skills": 5,
        "programming languages": 5,
        "projects": 8,
        "experience": 8,
        "education": 3,
        "certifications": 5
    }

    section_bonus = sum(b for s, b in sections.items() if s in text)

    final_score = min(score + section_bonus, 100)

    missing_skills = [s for s in SKILL_WEIGHTS if s not in found_skills]

    # Role prediction
    if any(s in found_skills for s in ["machine learning", "nlp", "pandas", "numpy"]):
        role = "Data Science / AI Engineer"
    elif any(s in found_skills for s in ["react", "html", "css", "javascript"]):
        role = "Frontend / Full Stack Developer"
    elif any(s in found_skills for s in ["java", "c", "c++", "sql"]):
        role = "Software Developer"
    else:
        role = "Beginner / Fresher"

    # Suggestions
    suggestions = []

    if final_score < 80:
        suggestions.append("Add real-world projects with GitHub links")
        suggestions.append("Learn Git & GitHub for version control")
        suggestions.append("Focus on one tech stack (Web / AI / Backend)")

    if "react" not in found_skills:
        suggestions.append("Learn React for frontend opportunities")

    if "sql" not in found_skills:
        suggestions.append("Learn SQL for backend/data roles")

    if "machine learning" not in found_skills:
        suggestions.append("Learn Machine Learning basics for AI roles")

    # Rating
    if final_score >= 80:
        rating = "Advanced ⭐⭐⭐"
    elif final_score >= 50:
        rating = "Intermediate ⭐⭐"
    else:
        rating = "Beginner ⭐"

    return found_skills, missing_skills, final_score, rating, role, suggestions