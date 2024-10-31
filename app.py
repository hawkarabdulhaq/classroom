import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Utility function to print or write depending on the environment
def output(message):
    if 'streamlit' in globals():
        st.write(message)
    else:
        print(message)

# Load CSV Data
def load_csv_data(filepath):
    try:
        data = pd.read_csv(filepath)
        output("CSV data loaded successfully.")
        return data
    except FileNotFoundError:
        output("CSV file not found.")
        return None

# Content Management Function
def content_management():
    output("Loading content management...")
    data = load_csv_data("content_data.csv")
    if data is not None:
        output(data)

# Authenticate Google Classroom
def authenticate_google_classroom():
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    output(f"Loading credentials from: {credentials_path}")

    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=[
                "https://www.googleapis.com/auth/classroom.courses",
                "https://www.googleapis.com/auth/classroom.coursework.students",
                "https://www.googleapis.com/auth/classroom.rosters"
            ]
        )
        output("Credentials successfully loaded.")
    except Exception as e:
        output(f"Error loading credentials: {e}")
        return None

    try:
        service = build("classroom", "v1", credentials=credentials)
        output("Google Classroom service initialized successfully.")
        return service
    except Exception as e:
        output(f"Error initializing Google Classroom service: {e}")
        return None

# Classroom Overview Function
def classroom_overview():
    output("Retrieving Google Classroom data...")

    service = authenticate_google_classroom()
    if service is None:
        output("Failed to authenticate with Google Classroom.")
        return

    try:
        classrooms = service.courses().list().execute().get("courses", [])
        if not classrooms:
            output("No classrooms found.")
            return

        for classroom in classrooms:
            output(f"Classroom: {classroom['name']}")

            try:
                coursework = service.courses().courseWork().list(courseId=classroom["id"]).execute().get("courseWork", [])
                if not coursework:
                    output("No content available for this classroom.")
                    continue

                for item in coursework:
                    output(f"Week {item.get('week', 'N/A')} - {item['title']}")
                    output(f"Type: {item.get('workType', 'N/A')}")
                    output(f"Description: {item.get('description', 'No description provided')}")
                    output(f"Link: {item.get('alternateLink', 'No link provided')}")
                    output("---")

            except Exception as e:
                output(f"Error retrieving coursework for {classroom['name']}: {e}")

    except Exception as e:
        output(f"Error retrieving classrooms: {e}")

# Main Function to Run App Logic
def main():
    output("Starting app.py to retrieve Google Classroom data...")
    content_management()
    classroom_overview()
    output("Finished running app.py.")

if __name__ == "__main__":
    main()
