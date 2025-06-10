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


print(" ")
artist = 'ABBA'
print("Only songs from", artist)
print(df[df['artist'] == artist])


print("\nBasic statistics:")
print(df.describe())  # Summary stats (count, mean, min, max for numeric columns)


print("\nMissing values:")
print(df.isnull().sum())  # Check for missing data

print("\nFirst 3 unique artists:")
print(df['artist'].unique()[:3])  # Unique values in artist column

# Additional practice: Count songs per artist
print("\nNumber of songs per artist (top 5):")
print(df['artist'].value_counts().head())

# Save filtered data
abba_songs.to_csv('data/abba_songs.csv', index=False)
print("\nSaved ABBA songs to data/abba_songs.csv")
print("\nSaved ABBA songs to data/abba_songs.csv")