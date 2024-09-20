import streamlit as st
import tempfile
import os

from cicero.utils.parsing import extract_text_from_pdf
from cicero.core import LLMClient
from cicero import templates as prompt

# Constants
LANGUAGE_OPTIONS = {
    "🇬🇧 English": "English",
    "🇮🇹 Italiano": "Italian",
    "🇫🇷 Français": "French",
    "🇩🇪 Deutsch": "German",
    "🇪🇸 Español": "Spanish"
}

#llm_client = LLMClient(
#    mode="local",
#    model="llama3",
#    url='http://localhost:11434/api/generate'
#)

from dotenv import load_dotenv
load_dotenv("./groq_api_key.env")

llm_client = LLMClient(
    mode="external",
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

def get_cv_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
    
    try:
        return extract_text_from_pdf(tmp_file_path)
    finally:
        os.unlink(tmp_file_path)

def parse_job_description(job_description):
    language = llm_client.query(prompt.detect_language.format(job_description))

    if language.lower().strip(".") != "english":
        translation = llm_client.query(prompt.translate.format(job_description))
        return translation
    else:
        return job_description


def get_similarity_score(job_description, cv_text):
    return llm_client.query(prompt.compute_similarity.format(job_description, cv_text))

def get_skill_analysis(job_description, cv_text):
    return llm_client.query(prompt.get_missing_skills.format(job_description, cv_text))

def generate_cover_letter(job_description, cv_text, language):
    return llm_client.query(prompt.write_cover_letter.format(job_description, cv_text, language))

def main():
    st.set_page_config(page_title="CV Analyzer", page_icon="📄")
    
    st.title('📄 CV Analyzer')
    st.markdown("---")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Job Description")
        job_description = st.text_area("Enter the job description:", height=200)
        
        # Move the "Analyze CV" button here
        analyze_button = st.button('🔍 Analyze CV', key='analyze_button')
        
        # Add a placeholder for the spinner
        spinner_placeholder = st.empty()

    with col2:
        st.subheader("📎 Upload CV")
        uploaded_file = st.file_uploader("Upload your CV (PDF)", type="pdf")
        
        st.subheader("🌐 Cover Letter Language")
        sel_lang = st.selectbox(
            "Select a language for the Cover Letter",
            list(LANGUAGE_OPTIONS.keys())
        )
        language = LANGUAGE_OPTIONS[sel_lang]

    st.markdown("---")

    # Create placeholder elements
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 Similarity Score")
        similarity_score_placeholder = st.empty()
        similarity_score_placeholder.info("Your similarity score will appear here after analysis.")
    
    with col2:
        st.subheader("🔍 Skill Analysis")
        skill_analysis_placeholder = st.empty()
        skill_analysis_placeholder.warning("Missing skills will be listed here after analysis.")

    st.subheader("✉️ Generated Cover Letter")
    cover_letter_placeholder = st.empty()
    cover_letter_placeholder.text_area("Your generated cover letter will appear here after analysis.", height=300, disabled=True)

    if analyze_button:
        if uploaded_file is not None and job_description:
            # Use the spinner placeholder
            with spinner_placeholder:
                with st.spinner('Analyzing your CV... 🕵️‍♂️'):
                    try:
                        cv_text = get_cv_text(uploaded_file)
                        
                        parsed_job_description = parse_job_description(job_description)
                        similarity_score = get_similarity_score(parsed_job_description, cv_text)
                        similarity_score_placeholder.info(similarity_score)
                        
                        skill_analysis = get_skill_analysis(parsed_job_description, cv_text)
                        skill_analysis_placeholder.warning(skill_analysis)

                        cover_letter = generate_cover_letter(parsed_job_description, cv_text, language)
                        cover_letter_placeholder.text_area("", cover_letter, height=300)
                    
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("⚠️ Please upload a CV and enter a job description to start the analysis.")

if __name__ == "__main__":
    main()