from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables as usual
# api_key = os.getenv("OPENAI_API_KEY")

# print(f"Your API key is: {api_key}")
from classes.chunker import Chunker

text_splitter = SemanticChunker(OpenAIEmbeddings())


file_path = "data/belmont_report.txt"
# file_path = "data/defining_research_with_human_subjects.txt"
# file_path = "data/history_ethical_principles.txt"


with open(file_path, 'r', encoding='utf-8') as f:
    doc = f.read()
    
# docs = text_splitter.create_documents([doc])

# print(type(doc))
# def number_paragraphs(text):
#     # Split the text into paragraphs
#     paragraphs = text.split('\n\n')
    
#     # Add numbering to each paragraph
#     numbered_paragraphs = []
#     for i, paragraph in enumerate(paragraphs, start=1):
#         numbered_paragraph = f"{i}. {paragraph}"
#         numbered_paragraphs.append(numbered_paragraph)
    
#     # Join the paragraphs back together
#     numbered_text = '\n\n'.join(numbered_paragraphs)
    
#     return numbered_text
# doc_numbered = number_paragraphs(doc)

# print(doc)

chunker = Chunker()
res = chunker.split(doc)
for title, text in res.items():
    print("-----------------------------")
    print(title)
    print(text)
    print("\n")
# for doc in res:
#     print("-----------------------------")
#     print(doc.page_content)
#     # print(doc)
#     print("\n")



