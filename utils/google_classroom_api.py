# test_google_classroom_api.py
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials from JSON (replace this with path to JSON file if needed)
credentials = service_account.Credentials.from_service_account_file(
    "path/to/your_service_account.json",
    scopes=[
        "https://www.googleapis.com/auth/classroom.courses",
        "https://www.googleapis.com/auth/classroom.coursework.students",
        "https://www.googleapis.com/auth/classroom.rosters"
    ]
)

# Initialize Google Classroom API service
service = build("classroom", "v1", credentials=credentials)

# Fetch and print the list of classrooms
try:
    courses = service.courses().list().execute().get("courses", [])
    if not courses:
        print("No classrooms found.")
    else:
        for course in courses:
            print("Found Classroom:", course["name"])
except Exception as e:
    print("Error accessing Google Classroom:", e)
