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