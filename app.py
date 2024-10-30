# app.py
import streamlit as st
from utils.csv_parser import load_csv_data
from utils.google_classroom_api import authenticate_google_classroom

# App title and configuration
st.set_page_config(page_title="Classroom Content Management", layout="wide")
st.title("Classroom Content Management")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Contents", "Classroom Overview"))

# Load and display CSV data on the "Contents" page
if page == "Contents":
    st.header("Content Management")
    data = load_csv_data("content_data.csv")  # Load CSV data
    if data is not None:
        st.write(data)  # Display data in table form
        # Additional posting options and Google Classroom integration can go here

# Display Classroom Overview on the "Classroom Overview" page
elif page == "Classroom Overview":
    st.header("Classroom Overview")
    authenticate_google_classroom()  # Authenticate with Google Classroom
    st.write("This page will show classrooms and posted content status.")
    # Additional functionality to display classroom summaries can go here
