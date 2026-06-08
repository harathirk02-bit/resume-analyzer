import streamlit as st
from utils.analyzer import extract_text, analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center;'>
        AI Resume Analyzer
    </h1>
    <p style='text-align:center;'>
        Upload your resume and get instant analysis
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    found_skills, missing_skills, score, rating = analyze_resume(text)

    st.success("Resume Analysis Completed Successfully")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Resume Score", f"{score}%")

    with col2:
        st.metric("Skills Found", len(found_skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))

    with col4:
        st.metric("Rating", rating)

    st.divider()

    st.subheader("Skills Detected")

    if found_skills:
        st.write(", ".join(found_skills))
    else:
        st.warning("No matching skills found")

    st.divider()

    st.subheader("Recommended Skills")

    if missing_skills:
        st.write(", ".join(missing_skills))
    else:
        st.success("Excellent Resume")

    st.divider()

    st.subheader("Resume Evaluation")

    if score >= 80:
        st.success(
            "Excellent Resume. Strong profile for internships and entry-level roles."
        )

    elif score >= 50:
        st.warning(
            "Good Resume. Add more technical skills and projects."
        )

    else:
        st.error(
            "Resume needs improvement. Add skills, projects, and certifications."
        )

else:
    st.info("Upload a PDF resume to begin analysis.")