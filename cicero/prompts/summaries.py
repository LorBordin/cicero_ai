job_analysis_prompt = \
    """ 
    Given the following job descriptions, performs the following operations:
    
    - get the information of the required education (level of education, area of studies)
    - extract the information of the required seniority (junior, mid, senior, ...)
    - Make a summary of the required tasks for the applicant.
    - make a list of the required hard skills
    - make a list of the required soft skills

    Job description: 

    {}
    
    Do not include any introduction, just ouput the summary formatted as follow:


    1. Education: [education - 5 words max]
    
    2. Job Title: [job/role name and required seniority - 5 words max]  

    3. Task: [required task - 1 phrase]

    4. Hard skills:
        - hard skill 1 [1 phrase]
        - hard skill 2 [1 phrase]
        - ... [max 5 items]

    5. Soft skills:
        - soft skill 1 [1 phrase]
        - soft skill 2 [1 phrase]
        - ... [max 5 items]

    """


resume_analysis_prompt = \
    """ 
    Given the following resume, performs the following operations:
    
    - get candidate highest education (level of education, area of studies)
    - assess the candidate current job (role and seniority)
    - list the candidate daily tasks in his/her daily job
    - make a summary of the candidate hard kills and list it. Do not focus only in the Skill section of the CV (if any)
    - make a list of the candidate soft skills

    Candidate resume: 

    {}
    
    Do no include any introduction, just ouput the summary formatted as follow:


    1. Education: [education - 5 words max]
    
    2. Job Title: [current job/role and seniority - 5 words max]  

    3. Task: [required task - 1 phrase]

    4. Hard skills:
        - hard skill 1 [1 phrase]
        - hard skill 2 [1 phrase]
        - ... [max 5 items]

    5. Soft skills:
        - soft skill 1 [1 phrase]
        - soft skill 2 [1 phrase]
        - ... [max 5 items]

    """