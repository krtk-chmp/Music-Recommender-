import pandas as pd

# Load the cleaned ABBA dataset
df = pd.read_csv('data/abba_songs_cleaned.csv')

# Verify load
print("First 5 rows of cleaned ABBA songs:")
print(df.head())
print("\nShape (rows, columns):")
print(df.shape)

# Feature 1: Word count in text
df['word_count'] = df['text'].str.split().str.len()
print("\nWord count stats:")
print(df['word_count'].describe())

# Feature 2: Average word length
df['avg_word_length'] = df['text'].str.split().apply(lambda x: sum(len(word) for word in x) / len(x) if len(x) > 0 else 0)
print("\nAverage word length stats:")
print(df['avg_word_length'].describe())

# Save with new features
df.to_csv('data/abba_songs_featured.csv', index=False)
print("\nSaved dataset with features to data/abba_songs_featured.csv")