# google_classroom_api.py
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

def authenticate_google_classroom():
    # Load credentials from the environment variable or default file path
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    print(f"Loading credentials from: {credentials_path}")  # Debugging statement

    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=[
                "https://www.googleapis.com/auth/classroom.courses",
                "https://www.googleapis.com/auth/classroom.coursework.students",
                "https://www.googleapis.com/auth/classroom.rosters"
            ]
        )
        print("Credentials successfully loaded.")
    except Exception as e:
        print(f"Error loading credentials: {e}")
        st.error("Failed to load Google Classroom credentials. Please check configuration.")
        return None

    # Initialize Google Classroom API service
    try:
        service = build("classroom", "v1", credentials=credentials)
        print("Google Classroom service initialized successfully.")
        return service
    except Exception as e:
        print(f"Error initializing Google Classroom service: {e}")
        st.error("Failed to initialize Google Classroom API service.")
        return None
