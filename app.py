# app.py
import streamlit as st
from pages.contents import content_management
from pages.classrooms import classroom_overview

st.set_page_config(page_title="Classroom Content Management", layout="wide")
st.title("Classroom Content Management")

st.sidebar.title("Navigation")

content_icon = "📚"
classroom_icon = "🏫"

contents_button = st.sidebar.button(content_icon + " Contents")
classroom_button = st.sidebar.button(classroom_icon + " Classroom Overview")

if contents_button:
    page = "Contents"
elif classroom_button:
    page = "Classroom Overview"
else:
    page = "Contents"

if page == "Contents":
    content_management()
elif page == "Classroom Overview":
    classroom_overview()
