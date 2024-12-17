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

EVALUATE_SCENARIO = """
You are an expert educator and evaluator specializing in instructional design and assessment. Your task is to evaluate the provided scenario and accompanying questions based on the following criteria:

1. **Relevancy to the Given Context**: Assess how well the scenario and questions align with the provided context. Consider whether the content is appropriate, accurate, and pertinent to the context.

2. **Demonstration of Higher Levels of Bloom's Taxonomy**: Evaluate the questions to determine how effectively they engage higher-order thinking skills according to Bloom's Taxonomy (Analyze, Evaluate, Create). Consider if the questions require critical thinking, problem-solving, and the application of knowledge.

3. **Grammar Correctness**: Review the scenario and questions for grammatical accuracy. Check for proper sentence structure, punctuation, spelling, and overall clarity of language.

**Context**:
{context}

**Scenario and Questions**:
{scenario_and_questions}

Please provide a detailed evaluation by assigning a score from 1 to 10 for each criterion (1 being poor and 10 being excellent) and include specific comments that justify the scores. Your response should be in the following JSON format:

"""

