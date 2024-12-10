

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
Try to ensure that each section should be at least 20 sentences long.

Input:
{document}: A piece of text that needs to be chunked into sections.
Output:
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

**Important:**
1. **Headings Structure:** 
   - Use Markdown syntax to create clear and hierarchical headings.
   - Use `#` for main sections (H1) if the summary covers multiple major topics.
   - Use `##` for sub-sections (H2) to delineate key points or categories within the main sections.
   - Ensure each heading accurately reflects the content of its corresponding section.

2. **Keyword Highlighting:** 
   - Identify and highlight key keywords in the summary by wrapping them in `<span>` tags with a specific background color.
   - Use the following format for highlighting: `<span style="background-color: #47b3b3;">keyword</span>`

Ensure that the summary maintains a logical flow, with headings appropriately segmenting the content to enhance readability and comprehension.

The goal is to create a summary that effectively communicates the context's content while being easily digestible and engaging.

CONTEXT: {document}
SUMMARY:
"""

SCENARIO_PROMPT = """
Based on the key themes, concepts, and findings in this paper, generate three distinct scenarios or domains that relate to the content. Each scenario should:
Explore different aspects, applications, or implications of the article.
Be unique and not overlap with the other scenarios.
Ensure that the scenarios are creative, relevant, and feasible, highlighting how they connect to the article findings.
"""

MULTI_CHOICE_PROMPT = """
Based on the following content, perform the following tasks:
1. Generate three distinct scenarios or domains that relate to the content. Each scenario should:
   - Be presented as a short paragraph.
   - Explore different aspects, applications, or implications of the article.
   - Be unique and not overlap with the other scenarios.
   - Ensure that the scenarios are creative, relevant, and feasible, highlighting how they connect to the article findings.
2. For each scenario, create three multiple-choice questions. Each question should have four options labeled 'A' to 'D', with only one correct answer.
3. Ensure that the questions accurately assess understanding of the scenario.

**Few-Shot Examples:**

**Content:** Implementing AI in Classroom Management

**Scenario 1:** Enhancing Personalized Learning through AI  
AI can revolutionize personalized learning by adapting educational content to fit each student's unique learning pace and style. This allows for more effective engagement and better academic outcomes.

**Questions:**
**Question 1:** What is a primary benefit of using AI for personalized learning?  
A) Reducing the need for teachers  
B) Personalizing learning experiences  
C) Increasing administrative workload  
D) Limiting student creativity  
**Answer:** B

**Question 2:** How can AI tools impact student engagement?  
A) By automating grading, making it less engaging  
B) By providing real-time feedback and interactive content  
C) By replacing all human interactions  
D) By restricting access to learning materials  
**Answer:** B

**Question 3:** What is a potential drawback of AI in personalized learning?  
A) Enhanced data privacy  
B) Improved teacher-student relationships  
C) Over-reliance on technology  
D) Increased manual tasks for teachers  
**Answer:** C

**Content:** {content_text}

**Scenarios and Questions:**
"""