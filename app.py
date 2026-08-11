import streamlit as st
import os
from src.resume_analyzer_agent.main import analyze_resume, compare_resume_job_description
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Resume Analyzer Agent",
    page_icon="📄",
)

st.title("Resume Analyzer Agent")

st.subheader("Resume Analysis")
st.caption("Analyze your resume to identify key skills, experience, strengths, and career opportunities.")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX Format)", 
    type=["pdf","docx"]
)

if uploaded_file:

    os.makedirs("resumes", exist_ok=True)

    file_path = os.path.join("resumes", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Resume uploaded: {uploaded_file.name}")

    target_role =st.text_area(
        "Enter your target role",
        height=50, 
        placeholder="e.g., Software Engineer, Data Scientist, Product Manager..."
    )
        
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            # result = run(file_path, target_role)
            result = analyze_resume(file_path, target_role)
            
        st.success("Resume analysis completed!")
        st.subheader("🔍 Resume Analysis Insights")
        st.write(result.raw)

    st.divider()

    st.subheader("Job Match Analysis")
    st.caption("See how well your resume matches the job requirements and identify skill gaps.")
    
    job_description = st.text_area(
    "Paste the job description here",
    height=300,
    placeholder="Paste the complete job description here..."
    )

    if st.button("Compare with job"):
        if not job_description.strip():
            st.warning("Please paste a job description to compare.")

        else:
            with st.spinner("Analyzing resume and comparing with job description..."):
                # result = run(file_path, job_description)
                result = compare_resume_job_description(file_path, job_description)
                st.success("Comparison completed!")
                st.subheader("🔍 Job Match Insights")
                st.write(result.raw)