import pandas as pd

# Load the dataset
df = pd.read_csv('data/spotify_million_songs.csv')  # Replace with your file name
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())