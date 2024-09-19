missing_skills_prompt = \
    """
    Given the following job description and CV, please identify the main skills required for the job that are missing in the CV.

    Job Description:
    {}

    CV:
    {}

    Format your response as follows:
    
    Missing Skills:
    - Skill 1
    - Skill 2
    - ...

    Do not include any additional output.
    """