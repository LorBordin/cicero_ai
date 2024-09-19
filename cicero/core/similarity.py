from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2, model):
    embedding1 = model.encode([text1])
    embedding2 = model.encode([text2])
    similarity = cosine_similarity(embedding1, embedding2)[0][0]
    return similarity