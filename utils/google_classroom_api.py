# google_classroom_api.py
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

def authenticate_google_classroom():
    # Load credentials from the GCP_SERVICE_ACCOUNT environment variable
    service_account_info = os.getenv("GCP_SERVICE_ACCOUNT")
    if service_account_info is None:
        raise ValueError("GCP_SERVICE_ACCOUNT environment variable is not set.")

    try:
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(service_account_info),
            scopes=[
                "https://www.googleapis.com/auth/classroom.courses",
                "https://www.googleapis.com/auth/classroom.coursework.students",
                "https://www.googleapis.com/auth/classroom.rosters"
            ]
        )
    except json.JSONDecodeError as e:
        raise ValueError("Failed to decode JSON from GCP_SERVICE_ACCOUNT. Please ensure the JSON is correctly formatted.") from e

    # Initialize Google Classroom API service
    service = build("classroom", "v1", credentials=credentials)
    return service
