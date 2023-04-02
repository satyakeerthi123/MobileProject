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
    names = ["K.Keerthi", "T.Poojitha","V.N.Karthik","G.Sruthi","K.Saran sai","N.Durga prasad","K.Sanjay","G.Sanjay"]

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
    if st.checkbox("show number of mobiles with RAM above 6GB "):
        st.write(data[data.RAM > 6])
    if st.checkbox("show number of mobile with RAM above 6 GB and BATTERY above 4000"):
        st.write(data[(data.RAM >6 ) & (data.battery> 4000)])
    if st.checkbox("show number of mobiles with STORAGE above 64 and SCREENSIZE above 6"):
        st.write(data[(data.storage > 64) & (data.screensize > 6)])
    if st.checkbox("show number of mobiles below the price of 800($) dollars"):
        st.write(data[data.price < 800])
    if st.checkbox("show number of mobiles with brand SAMSUNG and PRICE above $500 dollars"):
        st.write(data[(data.Brand=='samsung') & (data.price >500)])
    if st.checkbox("show number of mobiles with brand VIVO and screensize above 6.5"):
        st.write(data[(data.Brand=='vivo')&(data.screensize > 6.5)])
    if st.checkbox("show number of mobiles with battery capacity above 4500 and price below 700 dollars"):
        st.write(data[(data.battery>4500) & (data.price < 700)])
        

