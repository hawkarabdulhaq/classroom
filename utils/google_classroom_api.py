# google_classroom_api.py
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

def authenticate_google_classroom():
    # Load credentials from the GCP_SERVICE_ACCOUNT environment variable
    service_account_info = json.loads(os.getenv("GCP_SERVICE_ACCOUNT"))

    credentials = service_account.Credentials.from_service_account_info(
        service_account_info,
        scopes=[
            "https://www.googleapis.com/auth/classroom.courses",
            "https://www.googleapis.com/auth/classroom.coursework.students",
            "https://www.googleapis.com/auth/classroom.rosters"
        ]
    )

    # Initialize Google Classroom API service
    service = build("classroom", "v1", credentials=credentials)
    return service
