import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load resources
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
index = faiss.read_index('embed/healthcare_index.faiss')
df = pd.read_csv('data/healthcare_data.txt', sep='\t', encoding='utf-8')

def search_questions(query, k=10):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    results = []
    seen_answers = set()
    for idx, distance in zip(indices[0], distances[0]):
        if idx != -1:
            answer = df.iloc[idx]['Answers']
            if answer not in seen_answers:
                seen_answers.add(answer)
                results.append({
                    'question': df.iloc[idx]['Questions'],
                    'answer': answer,
                    'score': float(1 - distance)
                })
        if len(results) == 3:  # Only return top 3 unique answers
            break
    return results