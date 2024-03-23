import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



df_games = pd.read_excel('F5346D20.xlsx')

st.title('💾 - Our recommendations')

# Convert release_year to string type
df_games['release_year_str'] = df_games['release_year'].astype(str)

st.subheader("Key Insights on Game Success Factors")
top_games = df_games.nlargest(5, 'positive_ratings')[['name', 'positive_ratings', 'release_year_str']]
st.write(top_games)

# Positive Ratings Over Years～
st.subheader("Positive Ratings Over Years")
fig, ax = plt.subplots()
sns.lineplot(data=df_games, x='release_year', y='positive_ratings', ax=ax)
ax.set_title('Positive Ratings Trend Over Years')
st.pyplot(fig)


# Recommendations～
st.header("Strategic Recommendations for Game Developers and Publishers")
st.write("""
Based on our analysis, here are some strategic recommendations to enhance the success of video games on Steam:
1. **Genre Focus**: Invest in genres that consistently receive positive reviews and have growing popularity, such as Action games that seem pretty popular.
2. **Positive Ratings by Year of Release**: There is no clear correlation between the year of release and the number of positive ratings. This suggests that the success of a game, in terms of positive reviews, does not strongly depend on its release year.
3. **Most Reviews by Year of Release**: There is no clear correlation between the year of release and reviews with a high review ratio.  But with more and more games being released every year, the competition is getting fiercer.

""")


