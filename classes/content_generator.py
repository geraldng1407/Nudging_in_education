from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.output_parser import MermaidCode, Summary
from prompts.prompts import VISUAL_PROMPT, SUMMARY_PROMPT
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

    def create_summary(self, doc):
        self.llm = self.llm.bind_tools([Summary])
        prompt_description = ChatPromptTemplate.from_template(SUMMARY_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='Summary')

        self.parsed_job = (prompt_description | self.llm | parser)

        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke(
                {"document": doc, "word_count": "1000", "target_audience": "student"})
            if result and 'summary' in result[0]:
                return result[0]['summary']

        raise ValueError("Failed to generate summary after 5 attempts")
