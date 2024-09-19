import streamlit as st
import os
import tempfile
from sentence_transformers import SentenceTransformer

from cicero.core.similarity import calculate_similarity_llm
from cicero.core.cover_letter import generate_cover_letter
from cicero.utils.parsing import extract_text_from_pdf
from cicero.core.missing_skills import analyze_skills

# Initialize SentenceTransformer model
@st.cache_resource
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

model = load_model()

st.title('CV Analyzer')

# Job Description input
job_description = st.text_area("Enter the job description:")

# File uploader for CV
uploaded_file = st.file_uploader("Upload your CV (PDF)", type="pdf")

if st.button('Analyze') and uploaded_file is not None and job_description:
    with st.spinner('Analyzing...'):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        try:
            # Extract text from CV
            cv_text = extract_text_from_pdf(tmp_file_path)

            # Task 1: LLM-based similarity score
            similarity_score_llm = calculate_similarity_llm(job_description, cv_text)
            st.subheader("Similarity Score")
            st.write(f"{similarity_score_llm}")

            # Task 2: Skill analysis
            skill_analysis = analyze_skills(job_description, cv_text)
            st.subheader("Skill Analysis")
            st.write(skill_analysis)

            # Task 3: Generate cover letter
            cover_letter = generate_cover_letter(job_description, cv_text)
            st.subheader("Generated Cover Letter")
            st.text_area("", cover_letter, height=300)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            # Clean up temporary file
            os.unlink(tmp_file_path)
else:
    st.info("Please upload a CV and enter a job description to start the analysis.")

if __name__ == '__main__':
    # Streamlit runs this script directly
    pass