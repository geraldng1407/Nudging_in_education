from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Literal

class Keyword(BaseModel):
    keyword: str = Field(..., description="Keyword or phrases from the given text")
    
class Keywords(BaseModel):
    keywords: str = Field(..., description="A list of keywords or phrases from the given text")

class Evaluation(BaseModel):
    score: int = Field(..., description="Scoring based on the text from 1 to 10")
    confidence: int = Field(..., description="Confidence Score as a percentage")
    comments: str = Field(..., description="Brief comments to justify the score and confidence level")
    
class Evaluation_Scenario(BaseModel):
    relevancy_score: int = Field(..., description="Score based on relevancy to the given context")
    relevancy_comments: str = Field(..., description="Comments to justify the relevancy score")
    bloom_score: int = Field(..., description="Score based on the demonstration of higher levels of Bloom's Taxonomy")
    bloom_comments: str = Field(..., description="Comments to justify the Bloom's score")
    grammar_score: int = Field(..., description="Score based on grammar correctness")
    grammar_comments: str = Field(..., description="Comments to justify the grammar score")
    overall_score: int = Field(..., description="Overall score based on the evaluation")
    overall_comments: str = Field(..., description="Comments to justify the overall score")