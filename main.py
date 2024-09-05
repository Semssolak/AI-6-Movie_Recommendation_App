import streamlit as st
import numpy as np
import pandas as pd

# Load the data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('users.data', sep='\t', names=column_names)

movie_titles = pd.read_csv("movie_id_titles.csv")

# Merge dataframes
df = pd.merge(df, movie_titles, on='item_id')

# Pivot table to create user-item matrix
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

# Drop timestamp
df.drop(['timestamp'], axis=1, inplace=True)

# Calculate average rating and number of ratings
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['rating_oy_sayisi'] = pd.DataFrame(df.groupby('title')['rating'].count())

# Define a function to get similar movies
def get_recommendations(movie_name):
    try:
        # Get user ratings for the movie
        movie_user_ratings = moviemat[movie_name]

        # Get movies similar to the selected movie
        similar_movies = moviemat.corrwith(movie_user_ratings)

        # Create a DataFrame with correlation values
        corr_movies = pd.DataFrame(similar_movies, columns=['Correlation'])
        corr_movies.dropna(inplace=True)

        # Join with number of ratings
        corr_movies = corr_movies.join(ratings['rating_oy_sayisi'])

        # Filter out movies with less than 100 ratings and sort by correlation
        recommendations = corr_movies[corr_movies['rating_oy_sayisi'] > 100].sort_values('Correlation', ascending=False)

        return recommendations.head(6)  # Return top 5 similar movies
    except KeyError:
        return None

# Streamlit interface
st.title('Movie Recommendation System')

# Movie selection input
selected_movie = st.text_input('Enter a movie title you like:')

# Recommend button
if st.button('Recommend'):
    if selected_movie:
        recommendations = get_recommendations(selected_movie)
        if recommendations is not None:
            st.write(f"Movies similar to {selected_movie}:")
            for movie in recommendations.index[1:]:  # Skip the first one (it's the selected movie itself)
                st.write(movie)
        else:
            st.write("Movie not found in the dataset. Please try another one.")
    else:
        st.write("Please enter a movie title.")

#First, we must install it with the pip install streamlit command in the terminal.
#To run: streamlit run main.py in terminal in summer
#You can close the program with ctrl c