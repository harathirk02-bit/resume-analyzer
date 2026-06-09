import streamlit as st
from utils.analyzer import extract_text_from_pdf, analyze_resume

st.title("📄 ATS Resume Analyzer")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.text(resume_text)

    # Analyze resume
    found_skills, missing_skills, score, rating, role, suggestions = analyze_resume(resume_text)

    st.subheader("📊 Results")

    st.write("✅ Found Skills:", found_skills)
    st.write("❌ Missing Skills:", missing_skills)
    st.write("🎯 ATS Score:", score)
    st.write("⭐ Rating:", rating)
    st.write("💼 Suggested Role:", role)

    st.subheader("💡 Suggestions to Improve")

    for s in suggestions:
        st.write("👉", s)