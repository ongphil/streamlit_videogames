import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(
    page_title="Improvements",
    page_icon="🧩",
    layout="wide"
)


def load_data():
    return pd.read_excel("Steam Cleaned Data.xlsx")

df = load_data()
st.title('🧩 - Future improvements')

st.subheader('Cleaning data') 
st.write('Although our data set showed 0% errors in PowerBi and we removed any null columns, we faced the challenge of dealing with rows that had special characters. Our assumption is these characters come from improperly translated foreign words. In the future, it would be best to remove any rows with such values to ensure a higher quality of data, but we were unable to do so now.')


st.subheader('More cross-analysis') 
st.write('We limited our study to group by and count functions. Although we have added a correlation, we think we may need to cross different variables more in depth in order to get more relevant insights on the main drivers of success for video games.'
         'Moreover, some columns have not been used in our study, such as the publisher. In the future, such columns could be included to confirm some hypothesis.')


st.subheader('Make a more interactive webapp') 
st.write('This webapp displays our result but may lack some interctivity. For future improvements, it could be interesting to make graphs that highlights particular elements when hovering them, our make some elements stand out for more efficient visualization.')


st.subheader("Your Feedback")
feedback = st.text_area("Please provide your feedback here to help us improve:")
st.write("Thank you for your feedback!")