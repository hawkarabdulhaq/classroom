# csv_parser.py
import pandas as pd
import streamlit as st

def load_csv_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        st.error("CSV file not found.")
        return None
