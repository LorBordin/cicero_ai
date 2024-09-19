import streamlit as st
import os
import tempfile
from sentence_transformers import SentenceTransformer

from cicero.utils.parsing import extract_text_from_pdf
from cicero.templates import missing_skills_prompt
from cicero.templates import cover_letter_prompt
from cicero.templates import similarity_prompt, similarity_analysis_prompt
from cicero.templates import job_analysis_prompt, resume_analysis_prompt
from cicero.core import llm_query
from cicero.core import calculate_similarity

# Initialize SentenceTransformer model
@st.cache_resource
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

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

            # Task -2: Job description analysis
            job_analysis = llm_query(
                job_analysis_prompt.format(
                    job_description
                )
            )
            st.subheader("Job Summary")
            st.write(f"{job_analysis}")

            # Task -1: CV Analysis
            cv_analysis = llm_query(
                resume_analysis_prompt.format(
                    cv_text
                )
            )
            st.subheader("Resume Summary")
            st.write(f"{cv_analysis}")
            
            # Task 0: Similarity score based on summaries
            similarity_summaries = llm_query(
                similarity_analysis_prompt.format(
                    job_analysis,
                    cv_analysis
                )
            )
            st.subheader("Summaries")
            st.write(similarity_summaries)

            # Task 1: LLM-based similarity score
            similarity_score_llm = llm_query(
                similarity_prompt.format(
                    job_description, 
                    cv_text
                )
            )
            st.subheader("Similarity Score")
            st.write(f"{similarity_score_llm}")
            """
            # Task 2: Skill analysis
            skill_analysis = llm_query(
                missing_skills_prompt.format(
                    job_description,
                    cv_text
                )
            )
            st.subheader("Skill Analysis")
            st.write(skill_analysis)

            # Task 3: Generate cover letter
            cover_letter = llm_query(
                cover_letter_prompt.format(
                    job_description,
                    cv_text
                )
            )
            st.subheader("Generated Cover Letter")
            st.text_area("", cover_letter, height=300)
        """
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            # Clean up temporary file
            os.unlink(tmp_file_path)
else:
    st.info("Please upload a CV and enter a job description to start the analysis.")
