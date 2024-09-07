from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Literal

class Section(BaseModel):
    summary: str = Field(..., description="A short summary of the section in 1 line")
    title: str = Field(..., description="The title of what the section is about")
    text: str = Field(..., description="The text content of the section")
    
class Sections(BaseModel):
    sections: List[Section] = Field(..., description="A list of sections that have been extracted from the input text")

class Relevance(BaseModel):
    is_relevant: bool= Field(..., description="Whether the text is relevant to the specified topic")
    
class Index(BaseModel):
    start: int = Field(..., description="The starting index of the section")
    end: int = Field(..., description="The ending index of the section")
    title: str = Field(..., description="The title of the section")
    
class Indexes(BaseModel):
    indexes: List[Index] = Field(..., description="A list of indexes that have been extracted from the input text")
    
class MermaidCode(BaseModel):
    code: str = Field(..., description="The mermaid code that represents the visual representation of a provided segment of text as a mind map.")