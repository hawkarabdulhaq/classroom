# app.py
import streamlit as st
from pages.contents import content_management
from pages.classrooms import classroom_overview

# App title and configuration
st.set_page_config(page_title="Classroom Content Management", layout="wide")
st.title("Classroom Content Management")

# Sidebar with clickable icons
st.sidebar.title("Navigation")

# Define icons and labels
content_icon = "📚"
classroom_icon = "🏫"

# Display clickable icons as buttons in a vertical layout
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
    content_management()  # Loads content management from contents.py
elif page == "Classroom Overview":
    classroom_overview()  # Loads classroom overview from classrooms.py
