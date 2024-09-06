# CHUNKER_PROMPT = """
# Task: Chunk Text into Sections
# You are provided with a piece of text. Your task is to chunk the text into sections based on the content.
# At the start of each paragraph, there is a paragraph index. You will return the start and end index to group the paragraphs into sections.
# Input:
# {document}: A piece of text that needs to be chunked into sections.
# Output:
# """

CHUNKER_PROMPT = """
Task: Chunk Text into Sections
You are provided with a piece of text. Your task is to chunk the text into sections based on the content.
At the start of each paragraph, there is a paragraph index. You will return the start and end index to group the paragraphs into sections.
If the paragraph is irrelevant, you should not include it in the output. A paragrpah is irrelevant if it does not add to the main content of the text.
A paragraph is considered irrelevant if it contains any of the following:
Irrelevant Text Examples:
- Table of contents
- References
- Acknowledgements
- Author information
- Header Information
- Preface information

Example:
Input:

So far, several attempts have been made to achieve a gradual transfer towards autonomy using other options than external regulation.
Workplace simulations were implemented, intended to improve autonomous learning behavior in an environment reflecting the future workspace.
It became clear, however, that simply giving autonomy in these workplace simulations was not enough to promote students’ autonomous learning behavior.
Output: 'start': 1, 'end': 3, 'title': 'Attempts to Achieve Autonomy'

Input:
{document}: A piece of text that needs to be chunked into sections.
Output:
"""


RELEVANT_PROMPT = """
Task: Determine Text Relevance to a Specific Topic
You are provided with a piece of text. Your task is to assess whether this text is relevant to a specific topic or not.

Irrelevant Text Examples:
- Table of contents
- References
- Acknowledgements
- Author information
- Header Information
- Preface information

Input:
{document}: A segment of text that needs to be evaluated for its relevance to the specified topic.

Output:
Return True if the text is relevant.
Return False if the text is not relevant.
Please ensure your assessment is thorough and accurate.
"""
# RELEVANT_PROMPT = """
# You are given a piece of text. You task is to identify if the text is relevant to a specific topic or not.
# Some examples of text that are not relevant are text that includes table of contents, references, acknowledgements or authors.
# Inputs:

# {document}: A piece of text that needs to be evaluated for relevance to a specific topic.
# Output(True/False):
# """
