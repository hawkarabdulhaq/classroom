# app.py
import streamlit as st
from utils.csv_parser import load_csv_data
from utils.google_classroom_api import authenticate_google_classroom

# App title and configuration
st.set_page_config(page_title="Classroom Content Management", layout="wide")
st.title("Classroom Content Management")

# Sidebar with clickable icons
st.sidebar.title("Navigation")

# Define icons and labels
content_icon = "📚"
classroom_icon = "🏫"

# Display clickable icons in a vertical layout as buttons
contents_button = st.sidebar.button(content_icon + " Contents")
classroom_button = st.sidebar.button(classroom_icon + " Classroom Overview")

# Page routing based on button click
if contents_button:
    page = "Contents"
elif classroom_button:
    page = "Classroom Overview"
else:
    page = "Contents"  # Default to Contents page

# Display selected page content
if page == "Contents":
    st.header("Content Management")
    data = load_csv_data("content_data.csv")  # Load CSV data
    if data is not None:
        st.write(data)  # Display data in table form
        # Additional posting options and Google Classroom integration can go here

elif page == "Classroom Overview":
    st.header("Classroom Overview")
    authenticate_google_classroom()  # Authenticate with Google Classroom
    st.write("This page will show classrooms and posted content status.")
    # Additional functionality to display classroom summaries can go here
