import pandas as pd
import os  # Add this line at the top

try:
    df = pd.read_csv('data/healthcare_data.txt', delimiter='\t', encoding='utf-8')
    print("Dataset shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nFirst 3 rows:")
    print(df.head(3))
    
except Exception as e:
    print("Error:", e)
    print("\n⚠️ Files in data folder:")
    print(os.listdir('data'))  # Using os.listdir() instead of !dir here