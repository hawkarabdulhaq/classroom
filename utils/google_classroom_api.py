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
    
    # Test connection by printing the list of courses
    try:
        courses = service.courses().list().execute().get("courses", [])
        if not courses:
            print("No classrooms found.")
        else:
            print(f"Found {len(courses)} classrooms.")
    except Exception as e:
        print("Error accessing Google Classroom:", e)
    
    return service

