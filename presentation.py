import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.set_page_config(
    page_title="Presentation",
    page_icon="🎮",
    layout="wide"
)

st.title('🎮 - Steam Store Games')
st.write('*Elizabeth KAPLAN - Manon SARKIS - Hanjing SHI*')


st.subheader('About our data') 
st.write('We chose to work on Steam Games. This dataset was downloaded on **Kaggle.com** and contains 27,052 rows and 18 columns. The columns include information about the release_date, number of positive vs negative reviews, range of people owning the game, developers, publishers, genres and categories'
         'Through this dataset we would like to see any recurring tendencies in games, and see if some factors could explain their success')


df_games = pd.read_excel('F5346D20.xlsx')
st.dataframe(df_games)

st.subheader('Method used') 
st.write('For this study, we mainly used group by, sort values and count functions, as well as correlation coefficient')

st.subheader('Why this visualisation?') 
st.write('We chose to make graphs and dataframes in order to display our results. As the primary goal of our work is to explore the dataset and see most common factors, we used many count functions and group by.'
         'As there are a lot of data, it is also impossible to display everything in graphs while making it readable, which is the main reasons why we thought tables were more appropriate')


st.subheader('Bias') 
st.write('Our dataset is inherently biased, as the only games included are games that their primary release language is English and released in North America. The Steam platform accounts for only a fraction of video games as its only for PC gaming, and excludes console games. While our visualization can be representative of the PC English video games from 1997 - 2019, it is a limited scope of view.') 
(' According to a survey by WebTribunal, across platforms and languages there have been over 93,000 video games released since the conception of video games in 1958 with Table Tennis for Two.')
