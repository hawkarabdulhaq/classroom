import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Utility function for console output
def output(message):
    print(message)

# Load and display CSV data
def load_csv_data(filepath):
    try:
        data = pd.read_csv(filepath)
        output("CSV data loaded successfully.")
        output(data.to_string())  # Display the full DataFrame
        return data
    except FileNotFoundError:
        output("ERROR: CSV file not found.")
        return None

# Authenticate with Google Classroom API
def authenticate_google_classroom():
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
    if not os.path.exists(credentials_path):
        output(f"ERROR: {credentials_path} file not found!")
        return None

    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=[
                "https://www.googleapis.com/auth/classroom.courses",
                "https://www.googleapis.com/auth/classroom.coursework.students",
                "https://www.googleapis.com/auth/classroom.rosters"
            ]
        )
        output("Google Classroom credentials loaded successfully.")
        return build("classroom", "v1", credentials=credentials)
    except Exception as e:
        output(f"ERROR: Failed to initialize Google Classroom API - {e}")
        return None

# Retrieve and display Google Classroom data
def classroom_overview():
    service = authenticate_google_classroom()
    if service is None:
        output("ERROR: Google Classroom authentication failed.")
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
                output(f"ERROR: Failed to retrieve coursework for {classroom['name']} - {e}")

    except Exception as e:
        output(f"ERROR: Failed to retrieve classrooms - {e}")

# Main Function to Run App Logic
def main():
    output("Starting Google Classroom data retrieval and CSV loading...")
    
    # Display CSV content
    load_csv_data("content_data.csv")
    
    # Display Google Classroom content
    classroom_overview()

    output("Finished running app.py.")

if __name__ == "__main__":
    main()
