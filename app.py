import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load CSV Data
def load_csv_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("CSV data loaded successfully.")
        return data
    except FileNotFoundError:
        print("CSV file not found.")
        return None

# Content Management Function
def content_management():
    print("Loading content management...")
    data = load_csv_data("content_data.csv")
    if data is not None:
        print(data)

# Authenticate Google Classroom
def authenticate_google_classroom():
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    print(f"Loading credentials from: {credentials_path}")

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
        return None

    try:
        service = build("classroom", "v1", credentials=credentials)
        print("Google Classroom service initialized successfully.")
        return service
    except Exception as e:
        print(f"Error initializing Google Classroom service: {e}")
        return None

# Classroom Overview Function
def classroom_overview():
    print("Retrieving Google Classroom data...")

    service = authenticate_google_classroom()
    if service is None:
        print("Failed to authenticate with Google Classroom.")
        return

    try:
        classrooms = service.courses().list().execute().get("courses", [])
        if not classrooms:
            print("No classrooms found.")
            return

        for classroom in classrooms:
            print(f"Classroom: {classroom['name']}")

            try:
                coursework = service.courses().courseWork().list(courseId=classroom["id"]).execute().get("courseWork", [])
                if not coursework:
                    print("No content available for this classroom.")
                    continue

                for item in coursework:
                    print(f"Week {item.get('week', 'N/A')} - {item['title']}")
                    print(f"Type: {item.get('workType', 'N/A')}")
                    print(f"Description: {item.get('description', 'No description provided')}")
                    print(f"Link: {item.get('alternateLink', 'No link provided')}")
                    print("---")

            except Exception as e:
                print(f"Error retrieving coursework for {classroom['name']}: {e}")

    except Exception as e:
        print(f"Error retrieving classrooms: {e}")

# Main Function to Run App Logic
def main():
    print("Starting app.py to retrieve Google Classroom data...")

    # Check if running in a CI environment (like GitHub Actions)
    if os.getenv("CI") == "true":
        print("Running in a non-interactive environment.")
        classroom_overview()
        print("Finished retrieving classroom data.")
    else:
        # Interactive mode - displays contents and classroom overview
        print("Loading Content Management and Classroom Overview")
        content_management()
        classroom_overview()

    print("Finished running app.py.")

if __name__ == "__main__":
    main()
