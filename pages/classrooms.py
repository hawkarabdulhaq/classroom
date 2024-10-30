# classrooms.py
import streamlit as st
from utils.google_classroom_api import authenticate_google_classroom

def classroom_overview():
    st.header("Classroom Overview")

    # Authenticate and initialize Google Classroom API
    service = authenticate_google_classroom()
    
    # Retrieve list of all classrooms
    classrooms = service.courses().list().execute().get("courses", [])
    
    if not classrooms:
        st.write("No classrooms found.")
        return

    # Display each classroom and its contents
    for classroom in classrooms:
        st.subheader(classroom["name"])  # Display classroom name
        
        # Fetch coursework (assignments and questions) for this classroom
        coursework = service.courses().courseWork().list(courseId=classroom["id"]).execute().get("courseWork", [])
        
        if not coursework:
            st.write("No content available for this classroom.")
            continue
        
        # Display content details by week
        for item in coursework:
            st.write(f"**Week {item.get('week', 'N/A')} - {item['title']}**")
            st.write(f"Type: {item['workType']}")
            st.write(f"Description: {item.get('description', 'No description provided')}")
            st.write(f"Link: {item.get('alternateLink', 'No link provided')}")
            st.write("---")  # Separator for readability
