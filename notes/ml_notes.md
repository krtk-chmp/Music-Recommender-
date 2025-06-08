# ML Notes for Music Recommender

## Content-Based Filtering
- Recommends songs based on features like artist or song title.
- Example: If I like an ABBA song, suggest other ABBA songs.

## Cosine Similarity
- Measures similarity between song feature vectors (e.g., [artist=ABBA, song=title]).
- Value from -1 to 1; higher means more similar.
- Used with `sklearn.metrics.pairwise.cosine_similarity`.