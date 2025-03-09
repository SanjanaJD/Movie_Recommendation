import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data/top10K-TMDB-movies.csv')

# Display the first few rows of the dataframe
print(df.head())

# Describe the dataframe
print(df.describe())

# Check for null values
print(df.isnull().sum())

# Create a new dataframe with selected columns
movies = df[['id', 'title', 'genre', 'overview']]
movies['tags'] = movies['genre'] + movies['overview']

# Display the first few rows of the new dataframe
print(movies.head())

# Initialize CountVectorizer
cv = CountVectorizer(max_features=10000, stop_words='english')

# Convert tags into a vector form
vector = cv.fit_transform(movies['tags'].values.astype('U')).toarray()
print(vector.shape)

# Compute cosine similarity
similarity = cosine_similarity(vector)

# Function to find similar movies
def find_similar_movies(movie_title):
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
        similar_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
        return similar_movies
    except IndexError:
        print(f"Error: Movie '{movie_title}' not found in the dataset.")
        return []

# Function to print similar movies
def print_similar_movies(movie_title):
    similar_movies = find_similar_movies(movie_title)
    print(f"Movies similar to '{movie_title}':")
    for movie in similar_movies:
        print(movie)

# Example usage 
print_similar_movies("The Godfather")

# Save the similarity matrix and movies dataframe using pickle
with open('similarity.pkl', 'wb') as sim_file:
    pickle.dump(similarity, sim_file)
with open('movies.pkl', 'wb') as movies_file:
    pickle.dump(movies, movies_file)

print("Pickle files saved successfully.")