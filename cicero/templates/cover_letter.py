write_cover_letter = \
    """
    Given the following job description and CV, please generate a tailored cover letter for the candidate applying for this position. 
    The cover letter should highlight the candidate's relevant skills and experiences that match the job requirements, and express enthusiasm for the position.

    Job Description:
    {}

    CV:
    {}

    Please write a professional and concise cover letter (max 200 words).
    Please write the Cover Letter in {}.
    Format your answer as follow:
    
    [Greeting]

    [Opening paragraph: Express enthusiasm for the position and briefly mention how you learned about it]

    [Body paragraph 1: Highlight relevant skills and experiences that match the job requirements]

    [Body paragraph 2: Explain why you're interested in this specific role and company]

    [Closing paragraph: Thank the reader, express interest in an interview]

    [Closing]
    [Your Name]
    """