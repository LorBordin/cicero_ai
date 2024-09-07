missing_skills_prompt = \
    """
    Given the following job description and CV, please identify the skills required for the job that are not present in the CV. Also, provide brief suggestions on how to acquire these missing skills.

    Job Description:
    {}

    CV:
    {}

    Please format your response as follows:
    Missing Skills:
    - Skill 1
    - Skill 2
    - ...

    Suggestions for Skill Acquisition:
    - For Skill 1: [Brief suggestion]
    - For Skill 2: [Brief suggestion]
    - ...
    """