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
        
    if st.checkbox("Show number of times with mobile brand oppo and was exactly 128(GB)"):
        st.write(data[(data['Brand'] =='Oppo') & (data.Storage == 128)]) 
    if st.checkbox("show number of mobiles with RAM above 6GB "):
        st.write(data[data.RAM > 6])
    if st.checkbox("show number of mobile with RAM above 6 GB and BATTERY above 4000"):
        st.write(data[(data.RAM >6 ) & (data.Battery> 4000)])
    if st.checkbox("show number of mobiles with STORAGE above 64"):
        st.write(data[data.Storage > 64])
    if st.checkbox("show the mean of the Camera column"):
        st.write(data.groupby('Camera').mean())
    if st.checkbox("show number of mobiles with brand SAMSUNG and battery above 4500"):
        st.write(data[(data['Brand'] =='Samsung') & (data.Battery > 4500)])
    if st.checkbox("show number of mobiles with brand VIVO and RAM above 4"):
        st.write(data[(data['Brand']=='Vivo')&(data.RAM > 4)])
    if st.checkbox("show number of mobiles with battery capacity above 4500 and storage above 128gb"):
        st.write(data[(data.Battery >4500) & (data.Storage < 128)])
    if st.checkbox("show the mean of the battery column"):
        st.write(data.groupby('Battery').mean())
    if st.checkbox("show the mean of the Storage column"):
        st.write(data.groupby('Storage').mean())
    if st.checkbox("show the minimum value for Camera column"):
        st.write(data.groupby('Camera').min())
    if st.checkbox("show the maximum value for price column"):
        st.write(data.groupby('Price').max())
    if st.checkbox("show the standard deviation value for RAM column"):
        st.write(data.RAM.std())
    if st.checkbox("show the variance Battery column"):
        st.write(data.Battery.var())
    
    
        

