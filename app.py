import streamlit as st
from classes.chunker import Chunker

# Set page configuration
st.set_page_config(layout="wide")

# CSS to inject for centering the button
center_button_css = """
    <style>
    .centered-element {
        display: flex;
        justify-content: center;
    }

    /* Custom style for file uploader and selectbox */
    .stFileUploader > div:first-child,
    .stSelectbox > div:first-child {
        width: 100%;  /* Set desired width here */
        max-width: 600px; /* Adjust this value to set a maximum width */
        margin-left: auto;
        margin-right: auto;
    }
    </style>
"""

# Inject CSS with HTML
st.markdown(center_button_css, unsafe_allow_html=True)

# Centered upload button
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        uploaded_file = st.file_uploader("Upload", type=["txt", "docx"])

if uploaded_file is not None:
    
    if 'chunked_sections' not in st.session_state:
        
        # Read the file as a string and process only once
        doc = str(uploaded_file.read(), "utf-8")
        chunker = Chunker()
        
        chunked_sections = chunker.split(doc)
        
        section_titles = list(chunked_sections.keys())
        section_bodies = list(chunked_sections.values())
        
        # Store results in session state so they persist across reruns
        st.session_state.chunked_sections = chunked_sections
        st.session_state.section_titles = section_titles
        st.session_state.section_bodies = section_bodies
    
else:
   # Resetting session state if no file is uploaded or new file is selected
   if 'chunked_sections' in st.session_state:
       del st.session_state['chunked_sections']
       del st.session_state['section_titles']
       del st.session_state['section_bodies']
      
if 'section_titles' in st.session_state:
    
     selected_title = st.selectbox("Choose an option:", 
                                   options=st.session_state.section_titles)
     
     body_index=st.session_state.section_titles.index(selected_title)
     
     # Display content based on selection 
     st.write(f"You selected: {selected_title}")
     
     # Display text area with content corresponding to the selected title.
     body_content=st.text_area("", 
                               value=st.session_state.section_bodies[body_index], 
                               height=400)