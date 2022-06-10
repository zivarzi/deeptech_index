import streamlit as st
import pandas as pd
import pillow
import streamlit-aggrid

sheet_id = "1icwHkuyE9YUKMVwgwwdYM7iGJrKRV8cOBccCtN5UzV8"
sheet_name = "רשימת חברות"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv" # &sheet={sheet_name}"

df = pd.read_csv(url)

st.title("Welcome to the Israeli Deep-tech company index")
st.dataframe(df)