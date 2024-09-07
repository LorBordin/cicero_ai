from sentence_transformers import SentenceTransformer
import requests

from cicero.core.similarity import calculate_similarity_llm
from cicero.core.cover_letter import generate_cover_letter
from cicero.core.similarity import calculate_similarity
from cicero.utils.parsing import extract_text_from_pdf
from cicero.core.missing_skills import analyze_skills
    
    
def main():
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    print("Please enter the job description:")
    job_description = input()

    cv_path = input("Please enter the path to the CV (PDF format): ")

    try:
        cv_text = extract_text_from_pdf(cv_path)

        similarity_score = calculate_similarity(job_description, cv_text, model)
        print(f"\nJob Matching Score (embedding-based): {similarity_score:.4f}")

        print("\nCalculating LLM-based job matching score...")
        similarity_score_llm = calculate_similarity_llm(job_description, cv_text)
        print("Job Matching Score calculated by LLM:")
        print(similarity_score_llm)

        print("\nAnalyzing skills... This may take a moment.")
        skill_analysis = analyze_skills(job_description, cv_text)
        print("\nSkill Analysis Results:")
        print(skill_analysis)

        print("\nGenerating cover letter... This may take a moment.")
        cover_letter = generate_cover_letter(job_description, cv_text)
        print("\nGenerated Cover Letter:")
        print(cover_letter)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()