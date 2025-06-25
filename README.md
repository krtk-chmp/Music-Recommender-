# Music Recommender

## Overview
This project is a Python-based music recommendation system that suggests songs based on user preferences or song features using machine learning. The project aims to demonstrate skills in data science, machine learning, and software development. As a beginner in Python and ML, I’m using this project to learn data preprocessing, content-based filtering, and system integration, with the goal of understanding and explaining every component of the project.

## Project Goals
- Develop a recommendation system using content-based filtering (e.g., based on song features like genre, tempo).
- Learn and apply Python libraries: pandas, NumPy, scikit-learn, and Jupyter Notebook.
- Practice data preprocessing, exploratory data analysis (EDA), and ML algorithm implementation.
- Document the development process and learning outcomes for portfolio showcase.
- Host the project on GitHub with clear setup instructions and reproducible code.
- Explore Full Stack developement and gain relevant knowledge. 

## Current Status
As of Day 1 (June 5, 2025), the project is in the setup phase:
- Python environment configured with a virtual environment.
- Installed libraries: pandas, NumPy, scikit-learn, Jupyter.
- GitHub repository initialized with `.gitignore` and `requirements.txt`.

## Planned Features
- Load and preprocess a music dataset (e.g., Million Song Dataset or Spotify API data).
- Perform EDA to understand song features and user preferences.
- Implement a content-based recommendation algorithm.
- Create a simple command-line interface (CLI) for user interaction.
- Explore basic web development with Flask for a simple UI.
- Evaluate recommendations using metrics like precision.

## Technologies
- **Programming**: Python 3.8+
- **Libraries**: pandas (data manipulation), NumPy (numerical operations), scikit-learn (ML algorithms), Jupyter Notebook (EDA and experimentation)
- **Tools**: Git, GitHub, VS Code
- **Dataset**: - Spotify Million Song Dataset from Hugging Face (vishnupriyavr/spotify-million-song-dataset), 57,650 rows, including artist, song, and text data.
  
## Project Timeline
- **Days 1–3**: Environment setup, dataset selection, Python/ML refresher.
- **Days 4–8**: Data preprocessing and EDA.
- **Days 9–13**: Build and test recommendation algorithm.
- **Days 14–17**: Integrate system and create CLI (optional Flask UI).
- **Days 18–20**: Test, document, and polish for portfolio.

## Learning Journey
This project is a hands-on learning experience to deepen my understanding of:
- Python for data science and ML.
- Data preprocessing and feature engineering.
- Recommendation systems and similarity metrics.
- Basic web development with Flask.
- Project management with Git and clear documentation.

## Things I Did on Day 2
- Downloaded the Spotify Million Song Dataset (57,650 rows) from Hugging Face and stored it in the `data/` folder.
- Wrote and tested `load_data.py` to load the dataset using pandas, inspecting the first 5 rows and column details, and created a 10,000-row subset (`spotify_subset.csv`) for efficiency.
- Created `ml_notes.md` to summarize machine learning concepts, including content-based filtering and cosine similarity, based on beginner resources.
- Synced the repository with GitHub and pulling updates.

## Things I Did on Day 3
- Created and tested `python_practice.py` to reinforce basic Python skills, practicing dictionaries, loops, functions, and error handling with a sample song dataset.
- Enhanced `load_data.py` to explore the Spotify Million Song Dataset using pandas, performing tasks like filtering ABBA songs, checking missing values, and counting songs per artist.
- Successfully ran the updated script and saved a filtered dataset (`abba_songs.csv`), gaining hands-on experience with data manipulation.
- Committed and pushed both scripts to GitHub, ensuring my progress is tracked.
- Optionally explored converting the `.csv` to a table view in IntelliJ, experimenting with console output or a Jupyter Notebook to visualize the data.

## Things I Did on Day 4
- Inspected the ABBA song subset (113 songs) extracted from the Spotify Million Song Dataset to identify data quality.
- Cleaned the dataset by removing duplicate songs, standardizing song names to title case, and filtering out texts shorter than 10 characters.
- Saved the cleaned ABBA dataset as `abba_songs_cleaned.csv` for future use.
- Committed changes to GitHub to track progress.

## Things I Did on Day 5
- Created `preprocess.py` to extract features from the cleaned ABBA dataset.
- Added features: word count and average word length from song lyrics to enhance data for analysis.
- Saved the enhanced dataset as `abba_songs_featured.csv` for future use.
- Committed changes to GitHub to track progress.

## Things I Did on Day 6
- Created `eda.py` to perform Exploratory Data Analysis on the ABBA dataset.
- Visualized word count distribution and average word length using histograms and bar charts.
- Analyzed statistical summary: word count (mean 250.43, range 97–566), average word length (mean 3.99, range 3.06–4.96).
- Found a weak correlation (-0.02) between word count and average word length, indicating no strong relationship.
- Committed changes to GitHub to track progress.

## Things I Did on Day 7
- Enhanced `eda.py` to analyze common words in ABBA song lyrics with visualizations, identifying top words like "love".
- Optionally removed stop words (e.g., "the", "and") using NLTK to focus on meaningful terms.
- Started `model_prep.py` to prepare TF-IDF features from song lyrics for recommendation modeling, extracting approximately 500 features.
- Committed changes to GitHub to track progress.

## Contact
For feedback or questions, reach out via GitHub or at kartik.saraswat@ucdconnect.ie
