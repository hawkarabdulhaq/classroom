# contents.py
import streamlit as st
from utils.csv_parser import load_csv_data

def content_management():
    st.header("Content Management")
    data = load_csv_data("content_data.csv")
    if data is not None:
        st.write(data)
