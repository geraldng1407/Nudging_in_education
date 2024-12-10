
# File: Nudging_in_education/app.py

import streamlit as st
from classes.chunker import Chunker
from classes.content_generator import ContentGenerator
import streamlit.components.v1 as components
from prompts.prompts import MULTI_CHOICE_PROMPT
from classes.output_parser import ScenariosWithQuestions, ScenarioWithQuestions, Question
import os

# Function to create Mermaid code (unchanged)


def create_mermaid_code(code):
    return f"""
    <html>
    <head>
    <style>
    .mermaid {{
        display: grid;
        place-items: center;
        height: 100%;
    }}
    .mermaid svg {{
        max-width: 100%;
    }}
    </style>
    </head>
    <body>
    <pre class="mermaid">
    {code}
    </pre>
    <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true }});
    </script>
    </body>
    </html>
    """


def main():
    # Set page configuration
    st.set_page_config(layout="wide")

    # Centered upload button
    with st.container():
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            uploaded_file = st.file_uploader("Upload", type=["txt", "docx"])
            if uploaded_file is not None:
                if 'chunked_sections' not in st.session_state:
                    # Read the file as a string and process only once
                    if uploaded_file.type == "text/plain":
                        doc = uploaded_file.read().decode("utf-8")
                    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                        import docx
                        docx_document = docx.Document(uploaded_file)
                        doc = "\n\n".join(
                            [para.text for para in docx_document.paragraphs])
                    else:
                        st.error("Unsupported file type.")
                        doc = ""

                    if doc:
                        chunker = Chunker()
                        with col2:
                            with st.spinner('Uploading File...'):
                                chunked_sections = chunker.split(doc)
                                section_titles = list(chunked_sections.keys())
                                section_bodies = list(
                                    chunked_sections.values())
                                st.toast(
                                    'File uploaded successfully!', icon="✅")

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
        with col2:
            selected_title = st.selectbox(
                "Choose a section:",
                options=st.session_state.section_titles,
                index=None,
                placeholder="Select a section",
            )
            st.markdown("<hr style='border:1px solid #f0f0f0'>",
                        unsafe_allow_html=True)

            if selected_title is not None:
                st.header("Study Type")
                study_type = st.radio(
                    "Study Type",
                    ["Visual", "Summary", "Scenario"],  # Unified 'Scenario'
                    horizontal=True,
                    index=None,
                    label_visibility="collapsed"
                )
                content_generator = ContentGenerator()

                if "generated_content" not in st.session_state:
                    st.session_state.generated_content = {}

                key = (selected_title, study_type)

                if study_type == "Visual":
                    regenerate = st.button("Regenerate Mindmap")
                    if regenerate or key not in st.session_state.generated_content:
                        try:
                            mermaid_code = content_generator.create_visual(
                                st.session_state.section_bodies[st.session_state.section_titles.index(
                                    selected_title)]
                            )
                            st.session_state.generated_content[key] = mermaid_code
                        except ValueError as ve:
                            st.error(f"Error generating visual: {ve}")

                    if key in st.session_state.generated_content:
                        components.html(create_mermaid_code(
                            st.session_state.generated_content[key]), height=1000)

                elif study_type == "Summary":
                    regenerate = st.button("Regenerate Summary")
                    if regenerate or key not in st.session_state.generated_content:
                        try:
                            summary = content_generator.create_summary(
                                st.session_state.section_bodies[st.session_state.section_titles.index(
                                    selected_title)]
                            )
                            st.session_state.generated_content[key] = summary
                        except ValueError as ve:
                            st.error(f"Error generating summary: {ve}")

                    if key in st.session_state.generated_content:
                        summary_content = st.session_state.generated_content[key]
                        st.markdown(summary_content, unsafe_allow_html=True)

                elif study_type == "Scenario":
                    regenerate = st.button("Regenerate Scenario and Questions")
                    if regenerate or key not in st.session_state.generated_content:
                        try:
                            content_text = st.session_state.section_bodies[st.session_state.section_titles.index(
                                selected_title)]
                            scenarios = content_generator.create_scenarios_with_questions(
                                content_text)
                            st.session_state.generated_content[key] = scenarios
                        except ValueError as ve:
                            st.error(
                                f"Error generating scenarios and questions: {ve}")

                    if key in st.session_state.generated_content:
                        scenarios = st.session_state.generated_content[key]
                        for idx, scenario in enumerate(scenarios, start=1):
                            st.subheader(f"Scenario {idx}")
                            st.markdown(
                                f"\n\n{scenario.get('scenario')}", unsafe_allow_html=True)

                            st.markdown("**Questions:**")
                            user_answers = {}
                            for q_idx, question in enumerate(scenario.get("questions"), start=1):
                                question_number = f"Q{idx}.{q_idx}"

                                # Define option letters
                                option_letters = ['A', 'B', 'C', 'D']

                                # Ensure there are exactly four options
                                if len(question.get("options")) != 4:
                                    st.error(
                                        f"Question {question_number} does not have exactly four options.")
                                    continue

                                # Map letters to options
                                options_with_letters = {
                                    letter: option.strip() for letter, option in zip(option_letters, question.get("options"))
                                }

                                # Create a list of labels like "A) Option Text"
                                option_labels = [
                                    f" {text}" for letter, text in options_with_letters.items()]

                                # Use the option letters as the actual values
                                selected_letter = st.radio(
    f"**{question_number}: {question.get('question')}**", 
    options=option_letters,
    format_func=lambda x: option_labels[option_letters.index(x)], 
    key=f"{key}_{idx}_{q_idx}",
    index=None
)

                                user_answers[q_idx] = selected_letter

                            if st.button(f"Submit Answers for Scenario {idx}"):
                                st.subheader(f"Results for Scenario {idx}")
                                for q_idx, question in enumerate(scenario.get("questions"), start=1):
                                    selected = user_answers.get(q_idx, None)
                                    correct = question.get("answer")
                                    if selected == correct:
                                        st.success(
                                            f"Question {q_idx}: Correct!")
                                    else:
                                        # Find the correct option text for display
                                        try:
                                            correct_text = next(
                                                option for letter, option in zip(option_letters, question.get("options"))
                                                if letter == correct
                                            )
                                            st.error(f"Question {q_idx}: Incorrect.\nCorrect Answer: {correct_text}")

                                        except StopIteration:
                                            st.error(
                                                f"Question {q_idx}: Incorrect.  \n Correct Answer: {correct}")

                            st.markdown("---")  # Separator between scenarios


if __name__ == "__main__":
    main()
