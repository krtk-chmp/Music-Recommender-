import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the featured ABBA dataset
df = pd.read_csv('data/abba_songs_featured.csv')

# Verify load
print("First 5 rows of featured ABBA songs:")
print(df.head())
print("\nShape (rows, columns):")
print(df.shape)

# TF-IDF on text for similarity
tfidf = TfidfVectorizer(max_features=500, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['text'])
feature_names = tfidf.get_feature_names_out()
print("\nNumber of TF-IDF features:", tfidf_matrix.shape[1])