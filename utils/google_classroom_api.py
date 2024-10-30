# google_classroom_api.py
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

def authenticate_google_classroom():
    # Load credentials
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/classroom.courses",
                "https://www.googleapis.com/auth/classroom.coursework.students",
                "https://www.googleapis.com/auth/classroom.rosters"]
    )

    # Initialize Google Classroom API service
    service = build("classroom", "v1", credentials=credentials)
    return service
