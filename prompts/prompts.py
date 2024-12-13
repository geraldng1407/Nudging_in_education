

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



# VISUAL_PROMPT = """
# You are an advanced programming assistant who specializes in creating visual representations of data using code in various charting languages, particularly focusing on Mermaid.js. 
# You have a knack for transforming complex data structures and ideas into easy-to-understand mind maps, leveraging your extensive experience in coding and visualization.

# Your task is to generate Mermaid chart code that accurately visualizes the provided text as a mind map. Follow these steps:

# 1. Identify the **Main Topic** from the text.
# 2. Extract **Subtopics** relevant to the Main Topic.
# 3. Determine **Relationships** (e.g., connections between subtopics).
# 4. Note any **Additional Annotations or notes** for specific nodes if necessary.
# 5. **Enhance only the leaf nodes** with descriptive sentences to provide more context and clarity in the visualization. Non-leaf nodes should reflect the theme of their branches without additional descriptions.

# Make sure that the final output is structured correctly for Mermaid.js, focusing on clarity and ease of understanding in the visualization.

# **Input:**
# {document}: A segment of text that needs to be visualized as a mind map using Mermaid.js.

# **Output:**
# ```mermaid
# mindmap
#   root(Main Topic)
#     subtopic1(Subtopic 1)
#       detailA(Detail A: Explanation or information about Detail A.)
#       detailB(Detail B: Explanation or information about Detail B.)
#     subtopic2(Subtopic 2)
#       detailC(Detail C: Explanation or information about Detail C.)
# """

# VISUAL_PROMPT = """
# You are an advanced programming assistant who specializes in creating visual representations of data using code in various charting languages, particularly focusing on Mermaid.js. 
# You have a knack for transforming complex data structures and ideas into easy-to-understand mind maps, leveraging your extensive experience in coding and visualization.

# Your task is to generate Mermaid chart code that accurately visualizes the provided text as a mind map. Follow these steps:

# 1. Identify the **Main Topic** from the text.
# 2. Extract **Subtopics** relevant to the Main Topic.
# 3. Determine **Relationships** (e.g., connections between subtopics).
# 4. Note any **Additional Annotations or notes** for specific nodes if necessary.
# 5. **Enhance only the leaf nodes** with descriptive sentences to provide more context and clarity in the visualization. Non-leaf nodes should reflect the theme of their branches without additional descriptions.

# Additionally, consider the provided **Feedback** to refine the mind map for better clarity and effectiveness:
# 6. **Analyze Feedback:**
#     - Review each feedback entry's **rating** and **comments**.
#     - Identify common themes or recurring issues mentioned in the comments.
# 7. **Incorporate Feedback:**
#     - If ratings are below a certain threshold (e.g., below 4), prioritize addressing the issues mentioned in the comments.
#     - Adjust the complexity, clarity, or structure of the mind map based on the feedback.
#     - Ensure that the final visualization aligns more closely with user expectations and addresses previous shortcomings.

# Make sure that the final output is structured correctly for Mermaid.js, focusing on clarity and ease of understanding in the visualization.

# **Input:**
# {document}: A segment of text that needs to be visualized as a mind map using Mermaid.js.

# **Feedback:**
# {feedback}: A list of feedback objects in an array of json format. Each feedback object contains a 'rating' and 'comments' field.


# **Output:**
# ```mermaid
# mindmap
#   root(Main Topic)
#     subtopic1(Subtopic 1)
#       detailA(Detail A: Explanation or information about Detail A.)
#       detailB(Detail B: Explanation or information about Detail B.)
#     subtopic2(Subtopic 2)
#       detailC(Detail C: Explanation or information about Detail C.)
# """

VISUAL_PROMPT = """
You are an advanced programming assistant who specializes in creating visual representations of data using code in various charting languages, particularly focusing on Mermaid.js. 
You have a knack for transforming complex data structures and ideas into easy-to-understand mind maps, leveraging your extensive experience in coding and visualization.

Your task is to generate Mermaid chart code that accurately visualizes the provided text as a mind map. Follow these steps:

1. **Identify the Main Topic:**
   - Extract the primary subject or central theme from the input text.

2. **Extract Subtopics:**
   - Identify key subtopics that branch out from the Main Topic.
   - Ensure subtopics are distinct and cover all significant aspects of the Main Topic.

3. **Determine Relationships:**
   - Define how subtopics interconnect or relate to each other and to the Main Topic.
   - Establish hierarchical or associative links as appropriate.

4. **Add Additional Annotations or Notes:**
   - Include relevant notes for specific nodes to provide extra context where necessary.
   - Use annotations to clarify complex relationships or concepts.

5. **Enhance Leaf Nodes:**
   - For all leaf nodes (nodes without further sub-branches), add descriptive sentences that offer more context and clarity.
   - Ensure non-leaf nodes succinctly reflect the theme of their branches without additional descriptions.

6. **Analyze Feedback:**
   - **Review Feedback Entries:**
     - Examine each feedback object, focusing on both the 'rating' and 'comments' fields.
     - Note the numerical ratings to gauge overall satisfaction.
     - Carefully read comments to understand specific praises, concerns, or suggestions.
   - **Identify Common Themes:**
     - Look for recurring issues or frequently mentioned points in the comments.
     - Categorize feedback into positive aspects to retain and areas needing improvement.
   - **Prioritize Feedback:**
     - Focus on feedback with lower ratings (e.g., below 4) as these indicate significant areas for enhancement.
     - Address the most common or impactful issues first to ensure the most critical problems are resolved.

7. **Incorporate Feedback:**
   - **Adjust Complexity:**
     - Simplify overly complex sections or add necessary details to under-explained areas based on feedback.
   - **Enhance Clarity:**
     - Rephrase or restructure parts of the mind map that were found confusing or unclear.
   - **Improve Structure:**
     - Reorganize the hierarchy or relationships between nodes to better reflect logical connections as suggested by feedback.
   - **Address Specific Issues:**
     - Tackle particular points raised in the comments, ensuring that previous shortcomings are effectively resolved.
   - **Validate Alignment with Expectations:**
     - Ensure that the final mind map closely aligns with user expectations and effectively addresses all highlighted areas from the feedback.

Make sure that the final output is structured correctly for Mermaid.js, focusing on clarity and ease of understanding in the visualization.

**Input:**
{document}: A segment of text that needs to be visualized as a mind map using Mermaid.js.

**Feedback:**
{feedback}: A list of feedback objects in an array of JSON format. Each feedback object contains a 'rating' and 'comments' field.

**Output:**
```mermaid
mindmap
  root(Main Topic)
    subtopic1(Subtopic 1)
      detailA(Detail A: Explanation or information about Detail A.)
      detailB(Detail B: Explanation or information about Detail B.)
    subtopic2(Subtopic 2)
      detailC(Detail C: Explanation or information about Detail C.)
"""

# SUMMARY_PROMPT = """
# You are an expert summarizer and analyzer who can help me.
# Generate a concise and coherent summary from the given Context. 
# Condense the context into a well-written summary that captures the main ideas, key points, and insights presented in the context. 
# Prioritize clarity and brevity while retaining the essential information. 
# Aim to convey the context's core message and any supporting details that contribute to a comprehensive understanding. 
# Craft the summary to be self-contained, ensuring that readers can grasp the content even if they haven't read the context. 
# Provide context where necessary and avoid excessive technical jargon or verbosity.

# **Important:**
# 1. **Headings Structure:** 
#    - Use Markdown syntax to create clear and hierarchical headings.
#    - Use `#` for main sections (H1) if the summary covers multiple major topics.
#    - Use `##` for sub-sections (H2) to delineate key points or categories within the main sections.
#    - Ensure each heading accurately reflects the content of its corresponding section.

# 2. **Keyword Highlighting:** 
#    - Identify and highlight key keywords in the summary by wrapping them in `<span>` tags with a specific background color.
#    - Use the following format for highlighting: `<span style="background-color: #47b3b3;">keyword</span>`

# Ensure that the summary maintains a logical flow, with headings appropriately segmenting the content to enhance readability and comprehension.

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

3. **Analyze Feedback:**
   - **Review Feedback Entries:**
     - Examine each feedback object, focusing on both the 'rating' and 'comments' fields.
     - Note the numerical ratings to gauge overall satisfaction.
     - Carefully read comments to understand specific praises, concerns, or suggestions.
   - **Identify Common Themes:**
     - Look for recurring issues or frequently mentioned points in the comments.
     - Categorize feedback into positive aspects to retain and areas needing improvement.
   - **Prioritize Feedback:**
     - Focus on feedback with lower ratings (e.g., below 4) as these indicate significant areas for enhancement.
     - Address the most common or impactful issues first to ensure the most critical problems are resolved.

4. **Incorporate Feedback:**
   - **Adjust Summary Content:**
     - Simplify overly complex sections or add necessary details to under-explained areas based on feedback.
     - Ensure that all essential points are covered and that the summary aligns with user expectations.
   - **Enhance Clarity and Readability:**
     - Rephrase or restructure parts of the summary that were found confusing or unclear.
     - Improve the logical flow to make the summary more coherent and easy to follow.
   - **Improve Structure:**
     - Reorganize the headings and sections to better reflect logical connections or user-suggested flows.
     - Ensure that the hierarchy of information is intuitive and enhances comprehension.
   - **Address Specific Issues:**
     - Tackle particular points raised in the comments, ensuring that previous shortcomings are effectively resolved.
   - **Validate Alignment with Expectations:**
     - Ensure that the final summary closely aligns with user expectations and effectively addresses all highlighted areas from the feedback.

Ensure that the summary maintains a logical flow, with headings appropriately segmenting the content to enhance readability and comprehension.

The goal is to create a summary that effectively communicates the context's content while being easily digestible and engaging.

**Input:**
{document}: A segment of text that needs to be summarized.

**Feedback:**
{feedback}: A list of feedback objects in an array of JSON format. Each feedback object contains a 'rating' and 'comments' field.

**SUMMARY:**
```markdown
"""


SCENARIO_PROMPT = """
Based on the key themes, concepts, and findings in this paper, generate three distinct scenarios or domains that relate to the content. Each scenario should:
Explore different aspects, applications, or implications of the article.
Be unique and not overlap with the other scenarios.
Ensure that the scenarios are creative, relevant, and feasible, highlighting how they connect to the article findings.
"""

# MULTI_CHOICE_PROMPT = """
# Based on the following content, perform the following tasks:
# 1. Generate three distinct scenarios or domains that relate to the content. Each scenario should:
#    - Be presented as a short paragraph.
#    - Explore different aspects, applications, or implications of the article.
#    - Be unique and not overlap with the other scenarios.
#    - Ensure that the scenarios are creative, relevant, and feasible, highlighting how they connect to the article findings.
# 2. For each scenario, create three multiple-choice questions. Each question should have four options labeled 'A' to 'D', with only one correct answer.
# 3. Ensure that the questions accurately assess understanding of the scenario.

# **Few-Shot Examples:**

# **Content:** Implementing AI in Classroom Management

# **Scenario 1:** Enhancing Personalized Learning through AI  
# AI can revolutionize personalized learning by adapting educational content to fit each student's unique learning pace and style. This allows for more effective engagement and better academic outcomes.

# **Questions:**
# **Question 1:** What is a primary benefit of using AI for personalized learning?  
# A) Reducing the need for teachers  
# B) Personalizing learning experiences  
# C) Increasing administrative workload  
# D) Limiting student creativity  
# **Answer:** B

# **Question 2:** How can AI tools impact student engagement?  
# A) By automating grading, making it less engaging  
# B) By providing real-time feedback and interactive content  
# C) By replacing all human interactions  
# D) By restricting access to learning materials  
# **Answer:** B

# **Question 3:** What is a potential drawback of AI in personalized learning?  
# A) Enhanced data privacy  
# B) Improved teacher-student relationships  
# C) Over-reliance on technology  
# D) Increased manual tasks for teachers  
# **Answer:** C

# **Content:** {content_text}

# **Scenarios and Questions:**
# """


MULTI_CHOICE_PROMPT = """
Based on the following content, perform the following tasks:
1. **Generate Three Distinct Scenarios or Domains:**
   - Each scenario should be presented as a short paragraph.
   - Explore different aspects, applications, or implications of the article.
   - Ensure that each scenario is unique and does not overlap with the others.
   - The scenarios should be creative, relevant, and feasible, highlighting how they connect to the article's findings.

2. **Create Multiple-Choice Questions for Each Scenario:**
   - For each scenario, generate three multiple-choice questions.
   - Each question should have four options labeled 'A' to 'D', with only one correct answer.
   - Ensure that the questions accurately assess understanding of the scenario.

3. **Analyze Feedback:**
   - **Review Feedback Entries:**
     - Examine each feedback object, focusing on both the 'rating' and 'comments' fields.
     - Note the numerical ratings to gauge overall satisfaction.
     - Carefully read comments to understand specific praises, concerns, or suggestions.
   - **Identify Common Themes:**
     - Look for recurring issues or frequently mentioned points in the comments.
     - Categorize feedback into positive aspects to retain and areas needing improvement.
   - **Prioritize Feedback:**
     - Focus on feedback with lower ratings (e.g., below 4) as these indicate significant areas for enhancement.
     - Address the most common or impactful issues first to ensure the most critical problems are resolved.

4. **Incorporate Feedback:**
   - **Adjust Scenario Generation:**
     - Modify scenarios to address any concerns or suggestions mentioned in the feedback.
     - Ensure that scenarios are diverse and cover all significant aspects as per user expectations.
   - **Enhance Question Quality:**
     - Revise questions to improve clarity, relevance, and difficulty based on feedback.
     - Ensure that the correct answers are accurate and that distractors (incorrect options) are plausible.
   - **Improve Overall Structure and Clarity:**
     - Reorganize scenarios and questions for better logical flow and coherence.
     - Simplify overly complex scenarios or questions, or add necessary details to under-explained areas.
   - **Validate Alignment with Expectations:**
     - Ensure that the final scenarios and questions closely align with user expectations and effectively address all highlighted areas from the feedback.

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

**Feedback:**
{feedback}: A list of feedback objects in an array of JSON format. Each feedback object contains a 'rating' and 'comments' field.

**Scenarios and Questions:**
"""