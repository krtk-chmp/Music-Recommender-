import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the featured ABBA dataset
df = pd.read_csv('data/abba_songs_featured.csv')

# Verify load
print("First 5 rows of featured ABBA songs:")
print(df.head())
print("\nShape (rows, columns):")
print(df.shape)

# Extract common words from text
all_words = ' '.join(df['text']).lower().split()
common_words = Counter(all_words).most_common(10)
words, counts = zip(*common_words)

# Bar chart of common words
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='#FF69B4', edgecolor='#C71585')
plt.title('Top 10 Most Common Words in ABBA Songs')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in all_words if word not in stop_words and word.isalpha()]
common_filtered = Counter(filtered_words).most_common(10)
words_filtered, counts_filtered = zip(*common_filtered)

plt.figure(figsize=(10, 6))
plt.bar(words_filtered, counts_filtered, color='#20B2AA', edgecolor='#008B8B')
plt.title('Top 10 Most Common Non-Stop Words in ABBA Songs')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Visualization 1: Histogram of word count
plt.figure(figsize=(10, 6))
plt.hist(df['word_count'], bins=20, color='#1E90FF', edgecolor='#000080')
plt.title('Distribution of Word Count in ABBA Songs')
plt.xlabel('Word Count')
plt.ylabel('Number of Songs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Visualization 2: Bar chart of average word length
plt.figure(figsize=(10, 6))
plt.bar(range(len(df)), df['avg_word_length'], color='#32CD32', edgecolor='#006400')
plt.title('Average Word Length per Song')
plt.xlabel('Song Index')
plt.ylabel('Average Word Length')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Scatter plot of word_count vs avg_word_length
plt.figure(figsize=(10, 6))
plt.scatter(df['word_count'], df['avg_word_length'], color='#FF4500', alpha=0.6)
plt.title('Word Count vs Average Word Length')
plt.xlabel('Word Count')
plt.ylabel('Average Word Length')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Statistical summary
print("\nStatistical summary of features:")
print(df[['word_count', 'avg_word_length']].describe())

# Correlation between features
print("\nCorrelation between word_count and avg_word_length:")
print(df['word_count'].corr(df['avg_word_length']))