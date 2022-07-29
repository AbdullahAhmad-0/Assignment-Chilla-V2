import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''# **Data Analysis Web App**
This app is developed by Abdullah Ahmad Called **EDA**''')

with st.sidebar.header('Upload Your Dataset (csv)'):
    upload_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('iris')
    st.sidebar.markdown("[Example CSV File](https://google.com])")

def load_csv():
    csv = pd.read_csv(upload_file)
    return csv

def load_data():
    a = pd.DataFrame(np.random.rand(100, 5), columns=['age', 'banana', 'abdullah', 'dutchland', 'ear'])
    return a

def upload(a):
    if a == 0: df = load_csv()
    elif a == 1: df = load_data()
        
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('━━━━━━━━')
    st.header('**Profiling Report With Pandas**')
    st_profile_report(pr)

if upload_file != None: upload(0)
else:
    st.info('Waiting For File')
    if st.button('Press To Use Example Data'): upload(1)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ━━━━━━━╺━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━╺━━━