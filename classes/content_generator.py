from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_openai import ChatOpenAI

from classes.output_parser import MermaidCode, Summary, Scenarios, ScenariosWithQuestions
from prompts.prompts import VISUAL_PROMPT, SUMMARY_PROMPT, SCENARIO_PROMPT, MULTI_CHOICE_PROMPT
import os
import json
from dotenv import load_dotenv
load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o",
                              api_key=os.getenv("OPENAI_API_KEY"))
        self.sections = []
        # try:
        #     with open("./feedback.json", 'r', encoding='utf-8') as file:
        #         self.feedback = json.load(file)
        #         # print(self.feedback['Visual'])
        # except FileNotFoundError:
        #     print(f"Error: The file was not found.")
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding JSON: {e}")

    def create_visual(self, doc, feedback):
        self.llm = self.llm.bind_tools([MermaidCode])
        prompt_description = ChatPromptTemplate.from_template(VISUAL_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='MermaidCode')
        feedback_no_datetime = [{k: v for k, v in item.items() if k != 'datetime'} for item in feedback]
        self.parsed_job = (prompt_description | self.llm | parser)

        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke({"document": doc, "feedback": feedback_no_datetime})
            if result and 'code' in result[0]:
                return result[0]['code']

        raise ValueError("Failed to generate visual after 5 attempts")

    def create_summary(self, doc, feedback):
        self.llm = self.llm.bind_tools([Summary])
        prompt_description = ChatPromptTemplate.from_template(SUMMARY_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='Summary')
        feedback_no_datetime = [{k: v for k, v in item.items() if k != 'datetime'} for item in feedback]
        self.parsed_job = (prompt_description | self.llm | parser)

        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke(
                {"document": doc, "word_count": "1000", "target_audience": "student", "feedback": feedback_no_datetime})
            if result and 'summary' in result[0]:
                return result[0]['summary']

        raise ValueError("Failed to generate summary after 5 attempts")

    # def create_scenario(self, doc, prompt, feedback):
    #     print(doc)
    #     print(prompt)
    #     self.llm = self.llm.bind_tools([Scenarios])
    #     prompt_description = ChatPromptTemplate.from_template(prompt)
    #     parser = JsonOutputKeyToolsParser(key_name='Scenarios')

    #     self.parsed_job = (prompt_description | self.llm | parser)

    #     for _ in range(5):  # Retry up to 5 times
    #         result = self.parsed_job.invoke(
    #             {"document": doc, })
    #         if result and 'scenarios' in result[0]:
    #             return result[0]['scenarios']

    #     raise ValueError("Failed to generate scenarios after 5 attempts")
    
    def create_scenarios_with_questions(self, content_text, feedback):
        self.llm = self.llm.bind_tools([ScenariosWithQuestions])
        prompt_description = ChatPromptTemplate.from_template(MULTI_CHOICE_PROMPT)
        parser = JsonOutputKeyToolsParser(key_name='ScenariosWithQuestions')
        self.parsed_job = (prompt_description | self.llm | parser)
        feedback_no_datetime = [{k: v for k, v in item.items() if k != 'datetime'} for item in feedback]
        for _ in range(5):  # Retry up to 5 times
            result = self.parsed_job.invoke({"content_text": content_text, "feedback": feedback_no_datetime})
            if result and 'scenarios' in result[0]:
                return result[0]['scenarios']
        raise ValueError("Failed to generate scenarios and questions after 5 attempts")

