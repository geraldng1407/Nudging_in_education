from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.output_parser import Relevance, Indexes
from prompts.prompts import RELEVANT_PROMPT, CHUNKER_PROMPT
import os


class Chunker:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",
                              api_key=os.getenv("OPENAI_API_KEY"))
        self.sections = []

    # def relevancy(self, docs):
    #     self.llm = self.llm.bind_tools([Relevance])
    #     prompt_description = ChatPromptTemplate.from_template(RELEVANT_PROMPT)
    #     parser = JsonOutputKeyToolsParser(key_name='Relevance')

    #     self.parsed_job = (prompt_description | self.llm | parser)
    #     res = []
    #     for doc in docs:
    #         # print(doc.page_content)
    #         if self.parsed_job.invoke({
    #             "document": doc.page_content
    #         })[0]['is_relevant']:
    #             res.append(doc)
    #         # print("----------------")
    #     return res
    def number_paragraphs(self, text):
        # Split the text into paragraphs
        paragraphs = text.split('\n\n')
        
        # Add numbering to each paragraph
        numbered_paragraphs = []
        for i, paragraph in enumerate(paragraphs, start=1):
            numbered_paragraph = f"{i}. {paragraph}"
            numbered_paragraphs.append(numbered_paragraph)
        
        # Join the paragraphs back together
        numbered_text = '\n\n'.join(numbered_paragraphs)
    
        return numbered_text
    
    def split(self, doc):
        doc_numbered = self.number_paragraphs(doc)
        
        self.llm = self.llm.bind_tools([Indexes])
        prompt_description = ChatPromptTemplate.from_template(CHUNKER_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='Indexes')

        self.parsed_job = (prompt_description | self.llm | parser)
        indexes = self.parsed_job.invoke({
            "document": doc_numbered
        })[0]['indexes']
        # print(indexes)
        
        paragraphs = doc.split('\n\n')
        result = {}
        for index in indexes:
            result[index['title']] = "\n".join(paragraphs[index['start']:index['end']])
        return result

