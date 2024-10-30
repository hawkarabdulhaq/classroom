# contents.py
import streamlit as st
import pandas as pd
from utils.google_classroom_api import authenticate_google_classroom

def load_content(filepath="content_data.csv"):
    """Loads the content data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        st.error("CSV file not found.")
        return None

def content_management():
    st.header("Content Management")

    # Load content data
    data = load_content()
    if data is None:
        return

    # Display content grouped by Week
    weeks = data["Week"].unique()
    for week in sorted(weeks):
        st.subheader(f"Week {week}")

        # Filter data for the specific week
        week_data = data[data["Week"] == week]

        # Display each type of content (Material, Assignment, Question)
        for _, row in week_data.iterrows():
            st.markdown(f"### {row['Title']}")
            st.write(f"**Type:** {row['Type']}")
            st.write(row["Content"])

            # Display link if available
            if pd.notna(row["Link"]):
                st.write(f"[Link to resource]({row['Link']})")

            # Button to post content to Google Classroom
            if st.button(f"Post '{row['Title']}' to Classroom", key=f"{week}-{row['Title']}"):
                post_content_to_classroom(row)

            st.write("---")  # Separator for readability

def post_content_to_classroom(content_row):
    """Posts selected content to Google Classroom."""
    service = authenticate_google_classroom()
    
    # Placeholder for posting functionality: prepare data for API call
    classroom_id = "YOUR_CLASSROOM_ID"  # Replace with the specific Classroom ID or dynamically determine it
    course_work_body = {
        "title": content_row["Title"],
        "description": content_row["Content"],
        "materials": [{"link": {"url": content_row["Link"]}}] if pd.notna(content_row["Link"]) else [],
        "workType": "ASSIGNMENT" if content_row["Type"] == "Assignment" else "MATERIAL"
    }
    
    # API call to create course work
    try:
        service.courses().courseWork().create(courseId=classroom_id, body=course_work_body).execute()
        st.success(f"'{content_row['Title']}' posted successfully to Classroom.")
    except Exception as e:
        st.error(f"Failed to post '{content_row['Title']}': {e}")
