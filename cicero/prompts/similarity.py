compute_similarity = \
    """
    Given the following job description and CV, give a score between 0 and 100 that quantifies how much the candidate fits the role. 
    Also motivate your score.

    Job Description:
    {}

    CV:
    {}

    Please format your response as follows:
    ***Score:*** [score]

    ***Motivation:*** [motivation - 1 SENTENCE]
    """

compute_similarity_from_summary = \
    """
    Given the job description and resume summaries, provide a score between 0 and 100 to quantify how much the candidate fits the role.
    Also, motivate your score. Be precise and analytical, here is a list of aspects you should take into account:
        1. Candidate's education should be in the same or similar field and equal or higher to the required one. 
        2. Candidate's job title should be similar or in a similar field of the required one.
        3. Candidate's daily duties should have some overlap with the required, alternatively, based on his skills the candidate should be able to fullfill the required skills.
        4. Consider candidate's hard skills with the required ones.
        5. Consider candidate's soft skills with the required ones, if any.

    Job Summary:
    {}

    CV Summary:
    {}

    Please format your response as follows:
    
    Score: [score]

    Motivation: [motivation - 1 SENTENCE, NO LIST]
    """