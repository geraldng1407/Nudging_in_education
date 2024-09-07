from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.output_parser import MermaidCode
from prompts.prompts import VISUAL_PROMPT       
import os


class ContentGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",
                              api_key=os.getenv("OPENAI_API_KEY"))
        self.sections = []

    
    def create_visual(self, doc):
        self.llm = self.llm.bind_tools([MermaidCode])
        prompt_description = ChatPromptTemplate.from_template(VISUAL_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='MermaidCode')

        self.parsed_job = (prompt_description | self.llm | parser)
        
        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke({"document": doc})
            if result and 'code' in result[0]:
                return result[0]['code']
        
        raise ValueError("Failed to generate visual after 5 attempts")
        

