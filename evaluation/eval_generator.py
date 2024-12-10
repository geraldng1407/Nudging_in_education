from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from evaluation.output_parser import Keywords, Evaluation
from evaluation.prompts import KEYWORDS_PROMPT, EVALUATE_MINDMAP
import os


class EvalGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",
                              api_key=os.getenv("OPENAI_API_KEY"))
        self.sections = []

    def generate_keywords(self, doc):
        self.llm = self.llm.bind_tools([Keywords])
        prompt_description = ChatPromptTemplate.from_template(KEYWORDS_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='Keywords')

        self.parsed_job = (prompt_description | self.llm | parser)

        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke({"document": doc})
            if result and 'keywords' in result[0]:
                return result[0]['keywords']

        raise ValueError("Failed to generate keywords after 5 attempts")

    def evaluation_mindmap(self, mindmap, keywords):
        self.llm = self.llm.bind_tools([Evaluation])
        prompt_description = ChatPromptTemplate.from_template(EVALUATE_MINDMAP)
        parser = JsonOutputKeyToolsParser(key_name='Evaluation')

        self.parsed_job = (prompt_description | self.llm | parser)

        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke(
                {"mermaid": mindmap, "keywords": keywords})
            if result and 'score' in result[0]:
                return result[0]

        raise ValueError("Failed to generate eval after 5 attempts")
