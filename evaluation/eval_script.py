"""python -m evaluation.eval_script"""

import pandas as pd
import os
from evaluation.eval_generator import EvalGenerator
from classes.content_generator import ContentGenerator
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from deepeval.test_case import LLMTestCase

# Instantiate Eval_Generator once
eval_generator = EvalGenerator()
content_generator = ContentGenerator()


def generate_keywords_safe(doc):

    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        return eval_generator.generate_keywords(doc)
    except Exception as e:
        print(f"Error generating keywords for document: {e}")
        return ''  # Or handle as needed


def generate_mindmap_safe(doc):

    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        return content_generator.create_visual(doc)
    except Exception as e:
        print(f"Error generating keywords for document: {e}")
        return ''  # Or handle as needed


def generate_summary_safe(doc):
    if pd.isna(doc):
        return ''  # Handle NaN appropriately
    try:
        return content_generator.create_summary(doc)
    except Exception as e:
        print(f"Error generating keywords for document: {e}")
        return ''  # Or handle as needed


def evaluate_mindmap(mindmap, keywords):

    try:
        return eval_generator.evaluation_mindmap(mindmap, keywords)
    except Exception as e:
        print(f"Error generating keywords for document: {e}")
        return ''  # Or handle as needed


def evaluate_summary(text, summary):
    test_case = LLMTestCase(input=text, actual_output=summary)
    metric = SummarizationMetric(
        threshold=0.5,
        model="gpt-4o",
    )
    metric.measure(test_case)
    return {
        "score": metric.score,
        "comments": metric.reason
    }


def import_and_generate(input_file, output_file):
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

    # Apply the generate_keywords function to each row in the 'text' column

    print("Generating keywords for each section...")
    df['keywords'] = df['text'].apply(generate_keywords_safe)
    df['mindmap'] = df['text'].apply(generate_mindmap_safe)
    df['summary'] = df['text'].apply(generate_summary_safe)
    # Save the resulting DataFrame to a new CSV file
    try:
        df.to_csv(output_file, index=False)
        print(f"Keywords successfully saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not write to file {output_file}. {e}")


def evaluate(input_file, output_file):
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
    print("Generating keywords for each section...")
    eval_mindmap = df.apply(lambda row: evaluate_mindmap(
        row['mindmap'], row['keywords']), axis=1)
    # print(eval_mindmap)
    df['mindmap_score'] = eval_mindmap.apply(lambda x: x['score'])
    df['mindmap_confidence'] = eval_mindmap.apply(lambda x: x['confidence'])
    df['mindmap_comments'] = eval_mindmap.apply(lambda x: x['comments'])

    eval_summary = df.apply(lambda row: evaluate_summary(
        row['text'], row['summary']), axis=1)
    df['summary_score'] = eval_summary.apply(lambda x: x['score'])
    df['summary_comments'] = eval_summary.apply(lambda x: x['comments'])

    try:
        df.to_csv(output_file, index=False)
        print(f"Keywords successfully saved to {output_file}")
    except Exception as e:
        print(f"Error: Could not write to file {output_file}. {e}")


if not os.path.exists("./evaluation/data/test_new.csv"):
    import_and_generate("./evaluation/data/test.csv",
                        "./evaluation/data/test_new.csv")

evaluate("./evaluation/data/test_new.csv", "./evaluation/data/evaluation_1.csv")
