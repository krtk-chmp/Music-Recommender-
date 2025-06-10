# ML Notes for Music Recommender

## Content-Based Filtering
- Recommended based on the content consumed by the endhost.
- Recommends songs based on features like artist or song title.
- Example: If I like an ABBA song, suggest other ABBA songs.

## Cosine Similarity
- Mainly used for automation which we are trying to do in the project.
- Can analyse patterns (ratios) and express them into vectors.
- Make the vectors and plot them and the larger the angle, the more disassociated the two patterns are and least shows associativity.
- Cosine similarity is basically cos theta.  
- Transform the angle into the range 0-1 for which we use cosine.
- Measures similarity between song feature vectors (e.g., [artist=ABBA, song=title]).
- Value from -1 to 1; higher means more similar.
- ![formula]](image.png)



## Relevance to Project

- Feature Vectors: To use cosine similarity, you’ll turn song data into numerical vectors. For example:
- A song by “ABBA” with a “pop” genre might be a vector like [1, 0, 120] (1 for ABBA, 0 for another artist, 120 for tempo).
- Another ABBA song with tempo 125 might be [1, 0, 125].
- Cosine similarity compares these vectors to see how alike they are.
- Implementation: You’ll use sklearn.metrics.pairwise.cosine_similarity (noted in your ml_notes.md) to compute this. For instance, if a user likes an ABBA song, the system can find other songs with high cosine similarity scores based on artist and tempo.