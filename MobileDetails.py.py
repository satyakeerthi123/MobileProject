import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
logo = Image.open('logo1.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run weathertest.py 
st.set_page_config(page_title="Mobile  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
st.title("Exploratory Data Analysis on Modile Dataset")
# File upload
uploaded_file = st.file_uploader("Choose a Mobile Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
# Define the list of names
    names = ["", "", "","","","","V.N.Karthik"]

# Add the names to the sidebar
    st.sidebar.title("Project Team Members:")

    for name in names:
        st.sidebar.write(name)

    st.sidebar.title("Under The Guidance of :")
    st.sidebar.write("Dr.Bomma.Ramakrishna")
    st.title("Mobile Data Analysis")

    if st.checkbox("Show raw data"):
            st.write(data)

    if st.checkbox("Show first 25 rows"):
            st.write(data.head(25))

    if st.checkbox("Show shape"):
            st.write(data.shape)

    if st.checkbox("Show index"):
            st.write(data.index)

    if st.checkbox("Show columns"):
            st.write(data.columns)

    if st.checkbox("Show data types"):
            st.write(data.dtypes)

    if st.checkbox("Show unique values for 'Brands' column"):
            st.write(data['Brand'].unique())

    if st.checkbox("Show count of non-null values"):
            st.write(data.count())

    if st.checkbox("Show unique values count for each column"):
            st.write(data.nunique())

    if st.checkbox("Show unique models of'Apple'Brand"):
        st.write(data[data['Brand'] == 'Apple'])

    if st.checkbox("Show number of times 'Brand is exactly Google'"):
        st.write(data[data.Brand == 'Google'])
        
    if st.checkbox("Show number of times ' was exactly 128(GB)'"):
        st.write(data[(data['Brand'] =='Oppo') & (data.Storage == 128)])



