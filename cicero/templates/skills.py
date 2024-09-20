get_missing_skills = \
    """
    Given the following job description and CV, please identify the main skills required for the job that are missing in the CV.

    Job Description:
    {}

    CV:
    {}

    Format your response as follows:
    
    Consider improving the following skills:
    - Skill 1
    - Skill 2
    - ...

    Do not include any additional output.
    """