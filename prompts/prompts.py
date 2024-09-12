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

VISUAL_PROMPT = """
You are an advanced programming assistant who specializes in creating visual representations of data using code in various charting languages, particularly focusing on Mermaid.js. 
You have a knack for transforming complex data structures and ideas into easy-to-understand mind maps, leveraging your extensive experience in coding and visualization.

Your task is to generate Mermaid chart code that accurately visualizes the provided text as a mind map. Follow these steps:

1. Identify the **Main Topic** from the text.
2. Extract **Subtopics** relevant to the Main Topic.
3. Determine **Relationships** (e.g., connections between subtopics).
4. Note any **Additional Annotations or notes** for specific nodes if necessary.

Make sure that the final output is structured correctly for Mermaid.js, focusing on clarity and ease of understanding in the visualization.
Input:
{document}: A segment of text that needs to be visualized as a mind map using Mermaid.js.
Output:
"mermaid
mindmap
  root(Main Topic)
    subtopic1(Subtopic 1)
      detailA(Detail A)
      detailB(Detail B)
    subtopic2(Subtopic 2)
      detailC(Detail C)"
      
"""

# SUMMARY_PROMPT = """
# You are an expert summarizer and analyzer who can help me.
# Generate a concise and coherent summary from the given Context. 
# Condense the context into a well-written summary that captures the main ideas, key points, and insights presented in the context. 
# Prioritize clarity and brevity while retaining the essential information. 
# Aim to convey the context's core message and any supporting details that contribute to a comprehensive understanding. 
# Craft the summary to be self-contained, ensuring that readers can grasp the content even if they haven't read the context. 
# Provide context where necessary and avoid excessive technical jargon or verbosity.
# The goal is to create a summary that effectively communicates the context's content while being easily digestible and engaging.
# Summary should NOT be more than {word_count} words for {target_audience} audience.
# CONTEXT: {document}
# SUMMARY: 
# """

SUMMARY_PROMPT = """
You are an expert summarizer and analyzer who can help me.
Generate a concise and coherent summary from the given Context. 
Condense the context into a well-written summary that captures the main ideas, key points, and insights presented in the context. 
Prioritize clarity and brevity while retaining the essential information. 
Aim to convey the context's core message and any supporting details that contribute to a comprehensive understanding. 
Craft the summary to be self-contained, ensuring that readers can grasp the content even if they haven't read the context. 
Provide context where necessary and avoid excessive technical jargon or verbosity.
The goal is to create a summary that effectively communicates the context's content while being easily digestible and engaging.
CONTEXT: {document}
SUMMARY: 
"""
