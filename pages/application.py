import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from datetime import datetime

st.set_page_config(
    page_title="Application",
    page_icon="🕹️",
    layout="wide"
)

st.title('🕹️ - Results')


df_games = pd.read_excel('F5346D20.xlsx')


# Convert release_year to string type
df_games['release_year_str'] = df_games['release_year'].astype(str)

#map game releases over the years 
st.subheader('Steam game releases over the years') 
col1, col2 = st.columns(2)
with col1:
    release_year = []
    df_release_year = pd.DataFrame(release_year)
    df_release_year['count'] = df_games['name']
    df_release_year['release_year'] = df_games['release_year_str']
    count_release = df_release_year.groupby(by = ['release_year'])['count'].count()
    st.dataframe(count_release)
    
with col2:
    st.line_chart(count_release)


#Is there a correlation between the year the game came out and avg_owner?
st.subheader('Correlation') 
selected_columns = ['positive_ratings','negative_ratings','avg_owner','price','release_year']
df_subset = df_games[selected_columns]
fig_corr = plt.figure(figsize=(6, 4))
sns.heatmap(df_subset.corr(), annot=True, fmt='.2g')
st.pyplot(fig_corr)

# Calculate total reviews per game (use df_games)
df_games['total_reviews'] = df_games[['positive_ratings', 'negative_ratings']].sum(axis=1)

# Calculate positive review ratio
df_games['positive_ratio'] = df_games['positive_ratings'] / df_games['total_reviews']

# Sort by total reviews in descending order (highest first)
df_sorted_reviews = df_games.sort_values(by='total_reviews', ascending=False)

# Select the top 10 games
top_10_reviews = df_sorted_reviews.head(10)

# Display the top 10 games with most reviews and positive ratio
st.subheader('Top 10 Games with Most Reviews')
st.dataframe(top_10_reviews[['name', 'total_reviews', 'positive_ratio','genre_1']])



# Find games with over 1,000 total reviews
df_filtered = df_games[df_games[['positive_ratings', 'negative_ratings']].sum(axis=1) > 1000]

# Calculate positive ratings ratio
df_filtered['total_ratings_per_game'] = df_filtered[['positive_ratings', 'negative_ratings']].sum(axis=1)
df_filtered['positive_ratio'] = df_filtered['positive_ratings'] / df_filtered['total_ratings_per_game']

# Sort by positive ratio in descending order (highest first)
df_filtered = df_filtered.sort_values(by='positive_ratio', ascending=False)

# Display only specific columns
selected_columns = ['name', 'total_ratings_per_game', 'positive_ratio', 'genre_1', 'genre_2']
st.subheader('Games with Highest Positive Ratings Ratio (Over 1,000 Reviews)')
st.dataframe(df_filtered[selected_columns])
    

genre = []
df_genre = pd.DataFrame(genre)
df_genre['count'] = df_games[['appid']]
df_genre['genre'] = df_games['genre_1']
genre_count = df_genre['genre'].value_counts().sort_values(ascending=True)

fig_genre = plt.figure(figsize=(8, 6))
plt.barh(genre_count.index, genre_count.values, color = 'pink')
plt.xlabel("Nb of games per genre")
plt.ylabel("Genres")
plt.title("Count of different games per genre")
st.pyplot(fig_genre)