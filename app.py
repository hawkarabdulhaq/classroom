# app.py
import streamlit as st
from app_pages.contents import content_management
from app_pages.classrooms import classroom_overview


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
    st.session_state.page = "Contents"
elif classroom_button:
    st.session_state.page = "Classroom Overview"
else:
    # Use session_state to remember the selected page
    if 'page' not in st.session_state:
        st.session_state.page = "Contents"

# Display selected page content
if st.session_state.page == "Contents":
    content_management()  # Loads content management from contents.py
elif st.session_state.page == "Classroom Overview":
    classroom_overview()  # Loads classroom overview from classrooms.py
