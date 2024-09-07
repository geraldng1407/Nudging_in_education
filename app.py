import streamlit as st
from classes.chunker import Chunker
from classes.content_generator import ContentGenerator
import streamlit.components.v1 as components

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

mermaid_js = """
<html>
  <head>
    <style>
      .mermaid {
  display: grid;
  place-items: center;    /* Centers content both horizontally and vertically */
  height: 100%;           /* Ensure the container takes up full height if necessary */
}

.mermaid svg {
  max-width: 100%;
}
    </style>
  </head>
  <body>
    <pre class="mermaid">
            mindmap
  root((Boundaries Between Practice & Research))
    Definition of Practice
      - Solely to enhance well-being of individual patient or client
      - Reasonable expectation of success
      - Diagnosis, preventive treatment, or therapy to individuals
    Definition of Research
      - Designed to test a hypothesis and draw conclusions
      - Contributes to generalizable knowledge (theories, principles)
      - Described in a formal protocol with objectives and procedures
    Blurred Lines Between Practice and Research
      - Both often occur together (e.g., evaluating a therapy)
      - Notable departures from standard practice called "experimental"
    Innovation vs. Research
      - Significant departure from accepted practice is not automatically research
      - Experimental = new, untested, or different does not equal research 
        But should become formal research early on for safety and efficacy determination 
        Responsibility of medical practice committees to incorporate major innovations into formal research projects
    Combined Research and Practice Activities
      - Evaluating safety and efficacy of a therapy can be both practice and research 
        General rule: Any element of research requires review for protection of human subjects.
    </pre>

    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
      mermaid.initialize({ startOnLoad: true });
    </script>
  </body>
</html>
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


def create_mermaid_code(code):
    return """
<html>
  <head>
    <style>
      .mermaid {
  display: grid;
  place-items: center;    /* Centers content both horizontally and vertically */
  height: 100%;           /* Ensure the container takes up full height if necessary */
}

.mermaid svg {
  max-width: 100%;
}
    </style>
  </head>
  <body>
    <pre class="mermaid">
""" + code + """
    </pre>

    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
      mermaid.initialize({ startOnLoad: true });
    </script>
  </body>
</html>
"""


if 'section_titles' in st.session_state:

    selected_title = st.selectbox("Choose an section:",
                                  options=st.session_state.section_titles,
                                  index=None,
                                  placeholder="Select a section",)
    if selected_title is not None:
        study_type = st.radio(
            "Study Type", ["Visual", "Summary", "Scenario"], horizontal=True, index=None)
        content_generator = ContentGenerator()
        if "generated_content" not in st.session_state:
            st.session_state.generated_content = {}
        key = (selected_title, study_type)
        if study_type == "Visual":
            st.write("Visual")
            regenerate = st.button("Regenerate Mindmap")
            # components.html(mermaid_js, height=1000)
            if regenerate or key not in st.session_state.generated_content:
                st.session_state.generated_content[key] = content_generator.create_visual(
                    st.session_state.section_bodies[st.session_state.section_titles.index(selected_title)])
            components.html(create_mermaid_code(
                st.session_state.generated_content[key]), height=1000)
        elif study_type == "Summary":
            st.write("Summary")
        elif study_type == "Scenario":
            st.write("Scenario")
        # body_index = st.session_state.section_titles.index(selected_title)

        # # Display text area with content corresponding to the selected title.
        # body_content = st.text_area("",
        #                             value=st.session_state.section_bodies[body_index],
        #                             height=400)
