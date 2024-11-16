import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure consistent results from langdetect
DetectorFactory.seed = 0

def is_english(text):
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

def remove_non_english_rows(input_file, output_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Step 2: Detect language and filter rows
    df['is_english'] = df['Description'].apply(is_english)
    df = df[df['is_english']]

    # Step 3: Drop the helper column
    df = df.drop(columns=['is_english'])

    # Step 4: Write the filtered DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Filtered CSV file saved as {output_file}")

# Example usage
input_file = 'merged_news_articles.csv'
output_file = 'filtered_news_articles.csv'
remove_non_english_rows(input_file, output_file)