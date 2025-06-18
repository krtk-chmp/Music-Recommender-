import pandas as pd

# Load the dataset
df = pd.read_csv('data/spotify_million_songs.csv')  

# Pandas practice operations
print("First 10 rows of the dataset:") 
print(df.head(10))
print(" ")
print("Last 10 rows of the dataset:")
print(df.tail(10))

print(" ")
print("Number of rows and columns in the dataset:")
print(df.shape)

print(pd.isna(df))

print(" ")
print("Data types of each column:")
print(df.dtypes)

# Filter ABBA songs first
artist = 'ABBA'
print("\nOnly songs from", artist)
abba_songs = df[df['artist'] == artist]  # Define abba_songs 
print(abba_songs)
abba_songs.to_csv('data/abba_songs.csv', index=False)  
print("\nSaved ABBA songs to data/abba_songs.csv")

# Apply cleaning to ABBA songs
print("\nBasic statistics:")
print(abba_songs.describe())  # Summary stats

print("\nMissing values:")
print(abba_songs.isnull().sum())  # Check for missing data

print("\nFirst 10 unique artists (should be just ABBA):")
print(abba_songs['artist'].unique()[:10])  # Unique values

# Additional practice: Count songs per artist (should be 113 or less after cleaning)
print("\nNumber of songs per artist (top 5):")
print(abba_songs['artist'].value_counts().head())

# Check for case inconsistencies (False = consistent)
print("\nCase inconsistencies in artist:")
print(abba_songs['artist'].str.lower().nunique() != abba_songs['artist'].nunique())

# Check for extra spaces
print("\nRows with extra spaces in artist:")
print(abba_songs[abba_songs['artist'].str.contains(r'\s\s+')])

# DATA CLEANING for ABBA songs
abba_songs.drop_duplicates(subset=['song'], inplace=True)
print(f"\nRemoved duplicates, new row count: {len(abba_songs)}")

abba_songs['song'] = abba_songs['song'].str.strip().str.title()
print("\nStandardized song names")

# Calculate text_length and filter
abba_songs['text_length'] = abba_songs['text'].str.len()
abba_songs = abba_songs[abba_songs['text_length'] >= 10]
print(f"\nRemoved short texts, new row count: {len(abba_songs)}")

# Save cleaned ABBA songs
abba_songs.to_csv('data/abba_songs_cleaned.csv', index=False)
print("\nSaved cleaned ABBA songs to data/abba_songs_cleaned.csv")