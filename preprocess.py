import pandas as pd

# Load cleaned dataset
df = pd.read_csv('data/abba_songs_cleaned.csv')

# Extract feature: word count in text
df['word_count'] = df['text'].str.split().str.len()
print("First 5 rows with word count:")
print(df.head())

# Save with new feature
df.to_csv('data/abba_songs_featured.csv', index=False)
print("Saved dataset with word count to data/abba_songs_featured.csv")
