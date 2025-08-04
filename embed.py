import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

print("🔍 Loading embedding model...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

df = pd.read_csv('data/healthcare_data.txt', sep='\t', encoding='utf-8')
df = df.drop_duplicates(subset=['Questions'])  # Remove duplicate questions
texts = (df['Questions'] + " " + df['Answers']).tolist()

print("🛠 Creating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings.astype('float32'))

# Create directory if not exists
os.makedirs('embed', exist_ok=True)

print("💾 Saving FAISS index...")
try:
    faiss.write_index(index, 'embed/healthcare_index.faiss')
    print("✅ Index saved successfully!")
except Exception as e:
    print(f"❌ Error saving index: {e}")