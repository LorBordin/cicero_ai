similarity_prompt = \
"""
Given the following job description and CV, give a score between 0 and 100 that quantifies how much the candidate fits the role. Also motivate your score.
Job Description:
{}

CV:
{}

Please format your response as follows:
Candidate score: [score]

[motivation - 1 SENTENCE]
"""