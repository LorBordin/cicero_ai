write_cover_letter = \
    """
    Generate a professional cover letter tailored to the following job description and CV. 
    The cover letter should highlight the candidate's relevant skills and experiences, and express enthusiasm for the position.

    Job Description:
    {}

    CV:
    {}

    Write the letter in {} and format it in {} paragraphs. 
    Strictly adhere to the template below:

    {}

    Output only the letter text. Do not add any headers, introductions, or commentary.
    """