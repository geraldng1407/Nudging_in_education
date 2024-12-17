"""
python -m evaluation.eval_script
"""

import pandas as pd
import os
import asyncio
import nest_asyncio
from evaluation.eval_generator import EvalGenerator
from classes.content_generator import ContentGenerator
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from deepeval.test_case import LLMTestCase

# Instantiate EvalGenerator and ContentGenerator once
eval_generator = EvalGenerator()
content_generator = ContentGenerator()

# Adjusted functions to run synchronous code in async context
async def generate_keywords_safe(doc):
    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        loop = asyncio.get_event_loop()
        # Run the synchronous function in a thread pool executor
        return await loop.run_in_executor(None, eval_generator.generate_keywords, doc)
    except Exception as e:
        print(f"Error generating keywords for document: {e}")
        return ''  # Or handle as needed

async def generate_mindmap_safe(doc):
    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        loop = asyncio.get_event_loop()
        # Adjusted function call
        return await loop.run_in_executor(None, content_generator.create_visual, doc, [])
    except Exception as e:
        print(f"Error generating mindmap for document: {e}")
        return ''  # Or handle as needed

async def generate_summary_safe(doc):
    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        loop = asyncio.get_event_loop()
        # Adjusted function call
        return await loop.run_in_executor(None, content_generator.create_summary, doc, [])
    except Exception as e:
        print(f"Error generating summary for document: {e}")
        return ''  # Or handle as needed

async def generate_scenario_safe(doc):
    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        loop = asyncio.get_event_loop()
        # Adjusted function call
        return await loop.run_in_executor(None, content_generator.create_scenarios_with_questions, doc, [])
    except Exception as e:
        print(f"Error generating scenario for document: {e}")
        return ''  # Or handle as needed

async def evaluate_mindmap(mindmap, keywords):
    try:
        loop = asyncio.get_event_loop()
        # Adjusted function call
        return await loop.run_in_executor(None, eval_generator.evaluation_mindmap, mindmap, keywords)
    except Exception as e:
        print(f"Error evaluating mindmap: {e}")
        return {}

async def evaluate_scenario(context, scenario_and_questions):
    try:
        loop = asyncio.get_event_loop()
        # Adjusted function call
        return await loop.run_in_executor(None, eval_generator.evaluate_scenario, context, scenario_and_questions)
    except Exception as e:
        print(f"Error evaluating scenario: {e}")
        return {}

async def evaluate_summary(text, summary):
    try:
        test_case = LLMTestCase(input=text, actual_output=summary)
        metric = SummarizationMetric(
            threshold=0.5,
            model="gpt-4o",
        )
        loop = asyncio.get_event_loop()
        # Assuming metric.measure is synchronous
        await loop.run_in_executor(None, metric.measure, test_case)
        return {
            "score": metric.score,
            "comments": metric.reason
        }
    except Exception as e:
        print(f"Error evaluating summary: {e}")
        return {"score": "", "comments": ""}

# Async function to process a single row for generation
async def process_row_generate(row):
    text = row['text']
    # Run the generation tasks concurrently
    keywords_task = asyncio.create_task(generate_keywords_safe(text))
    mindmap_task = asyncio.create_task(generate_mindmap_safe(text))
    summary_task = asyncio.create_task(generate_summary_safe(text))
    scenario_task = asyncio.create_task(generate_scenario_safe(text))

    # Await the results
    row['keywords'] = await keywords_task
    row['mindmap'] = await mindmap_task
    row['summary'] = await summary_task
    row['scenario_and_questions'] = await scenario_task

    return row

# Async function to process a single row for evaluation
async def process_row_evaluate(row):
    text = row['text']
    mindmap = row.get('mindmap', '')
    keywords = row.get('keywords', '')
    summary = row.get('summary', '')
    scenario_and_questions = row.get('scenario_and_questions', '')

    # Run the evaluation tasks concurrently
    mindmap_task = asyncio.create_task(evaluate_mindmap(mindmap, keywords))
    summary_task = asyncio.create_task(evaluate_summary(text, summary))
    scenario_task = asyncio.create_task(evaluate_scenario(text, scenario_and_questions))

    # Await the results
    eval_mindmap = await mindmap_task
    eval_summary = await summary_task
    eval_scenario = await scenario_task

    # Populate evaluation results into the row
    row['mindmap_score'] = eval_mindmap.get('score', '')
    row['mindmap_confidence'] = eval_mindmap.get('confidence', '')
    row['mindmap_comments'] = eval_mindmap.get('comments', '')

    row['summary_score'] = eval_summary.get('score', '')
    row['summary_comments'] = eval_summary.get('comments', '')

    row['relevancy_score'] = eval_scenario.get('relevancy_score', '')
    row['relevancy_comments'] = eval_scenario.get('relevancy_comments', '')
    row['bloom_score'] = eval_scenario.get('bloom_score', '')
    row['bloom_comments'] = eval_scenario.get('bloom_comments', '')
    row['grammar_score'] = eval_scenario.get('grammar_score', '')
    row['grammar_comments'] = eval_scenario.get('grammar_comments', '')
    row['overall_score'] = eval_scenario.get('overall_score', '')
    row['overall_comments'] = eval_scenario.get('overall_comments', '')

    return row

# Async function to import and generate content
async def import_and_generate_async(input_file, output_file):
    try:
        # Read the input CSV file
        df = pd.read_csv(input_file, encoding='unicode_escape')
        print(f"Successfully read {input_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file {input_file} is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file {input_file} does not appear to be in CSV format.")
        return

    # Check if 'text' column exists
    if 'text' not in df.columns:
        print("Error: The input CSV does not contain a 'text' column.")
        return

    print("Generating content for each section asynchronously...")
    rows = df.to_dict('records')
    # Create tasks for all rows
    tasks = [process_row_generate(row) for row in rows]

    # Use asyncio.gather to run tasks concurrently
    results = await asyncio.gather(*tasks)

    # Create a new DataFrame from the results
    df_output = pd.DataFrame(results)

    # Save the resulting DataFrame to a new CSV file
    try:
        df_output.to_csv(output_file, index=False)
        print(f"Generated content successfully saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not write to file {output_file}. {e}")

# Async function to perform evaluation
async def evaluate_async(input_file, output_file):
    try:
        # Read the input CSV file
        df = pd.read_csv(input_file, encoding='unicode_escape')
        print(f"Successfully read {input_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file {input_file} is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file {input_file} does not appear to be in CSV format.")
        return

    print("Evaluating content asynchronously...")
    rows = df.to_dict('records')
    # Create tasks for all rows
    tasks = [process_row_evaluate(row) for row in rows]

    # Use asyncio.gather to run tasks concurrently
    results = await asyncio.gather(*tasks)

    # Create a new DataFrame from the results
    df_output = pd.DataFrame(results)

    # Save the evaluation results to a new CSV file
    try:
        df_output.to_csv(output_file, index=False)
        print(f"Evaluation successfully saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not write to file {output_file}. {e}")

# Main execution logic
async def main():
    if not os.path.exists("./evaluation/data/generated_content.csv"):
        await import_and_generate_async("./evaluation/data/raw_text.csv",
                                        "./evaluation/data/generated_content.csv")
    await evaluate_async("./evaluation/data/generated_content.csv",
                         "./evaluation/data/final_evaluation.csv")

# Run the main function using asyncio
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "asyncio.run() cannot be called from a running event loop" in str(e):
            # For environments like Jupyter Notebook
            nest_asyncio.apply()
            asyncio.get_event_loop().run_until_complete(main())
        else:
            raise e