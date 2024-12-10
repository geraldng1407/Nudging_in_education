KEYWORDS_PROMPT = """
You are an expert text analyzer. Your task is to extract the most relevant keywords and key phrases from the provided text.
Input: {document}
"""

EVALUATE_MINDMAP = """
You are an evaluator tasked with assessing a mindmap based on how well it incorporates a specific list of keywords. 
Your evaluation should focus on the presence, relevance, and representation of each keyword within the mindmap. 
After reviewing, provide a score between 1 and 10, where 10 signifies that the mindmap fully and effectively encapsulates all the keywords. 
Additionally, include a confidence score (as a percentage) indicating how certain you are about the assigned score.
Mindmap Code: {mermaid}
List of Keywords: {keywords}
Output(JSON):
"""

