# Nudging in Education Application Documentation
This application leverages the capabilities of the GPT-4.0 language model to assist instructors, educators, or researchers in better understanding and visualizing educational documents. It breaks down educational materials into manageable sections, generates visualizations, and produces summaries to enhance the teaching and learning experience.

## Table of Contents
- Installation
- Usage
- Modules
    - Chunker
    - Content Generator
    - Output Parser
    - Prompts
Streamlit Application
Contributing
License

## Installation
To get started with this project, make sure you have Python installed.
Make sure you have an OpenAI API key. Set your API key as an environment variable:
```export OPENAI_API_KEY='your_openai_api_key'```

## Usage
1. Run the Application:
Run the Streamlit application using the following command:
```streamlit run app.py```
2. Upload a Document:
Once the application is running, you can upload a text or docx file that needs to be processed.
3. View and Interact with Content:
The application will split the document into sections, and you can choose to generate summaries or visual representations of each section.

## Modules
### Chunker (chunker.py)
The Chunker class handles the segmentation of text into meaningful sections based on the context of the content.
### Content Generator (content_generator.py)
The ContentGenerator class is responsible for creating visualizations and summaries from document sections.
### Output Parser (output_parser.py)
Defines data models for processing and validating the outputs.
### Prompts (prompts.py)
Defines prompts for chunking text, generating visualizations, and summarizing content.

## Streamlit Applciation
The Streamlit application provides the graphical user interface for users to upload documents, view chunked sections, and generate visual or summarized content.





