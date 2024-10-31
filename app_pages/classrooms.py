# classrooms.py
import streamlit as st
from utils.google_classroom_api import authenticate_google_classroom

def classroom_overview():
    st.header("Classroom Overview")

    # Authenticate and initialize Google Classroom API
    service = authenticate_google_classroom()
    if service is None:
        st.write("Failed to authenticate with Google Classroom.")
        return
    
    # Retrieve list of all classrooms
    try:
        classrooms = service.courses().list().execute().get("courses", [])
        print(f"Retrieved classrooms: {classrooms}")  # Debugging output
    except Exception as e:
        print(f"Error retrieving classrooms: {e}")
        st.error("Failed to retrieve classrooms from Google Classroom.")
        return

    if not classrooms:
        st.write("No classrooms found.")
        return

    # Display each classroom and its contents
    for classroom in classrooms:
        st.subheader(classroom["name"])  # Display classroom name
        print(f"Classroom found: {classroom['name']}")  # Debugging output

        # Fetch coursework (assignments and questions) for this classroom
        try:
            coursework = service.courses().courseWork().list(courseId=classroom["id"]).execute().get("courseWork", [])
            print(f"Retrieved coursework for {classroom['name']}: {coursework}")  # Debugging output
        except Exception as e:
            print(f"Error retrieving coursework for {classroom['name']}: {e}")
            st.write(f"Failed to retrieve coursework for {classroom['name']}.")
            continue
        
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
