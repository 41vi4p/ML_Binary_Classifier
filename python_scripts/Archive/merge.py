import pandas as pd

def merge_columns(input_file, output_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Print column names to debug
    print("Column names:", df.columns)

    # Step 2: Merge the columns into a single 'Description' column
    #df['Description'] = df['Headline'].fillna('') + ' ' + df['Description'].fillna('') + ' ' + df['Article text'].fillna('')
    #df['Description'] = df['title'].fillna('') + ' ' + df['content'].fillna('')

    # Step 3: Drop the original columns
    df = df.drop(columns=['id'])

    # Step 4: Write the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Updated CSV file saved as {output_file}")

# Example usage
input_file = '3.csv'
output_file = 'merged_news_articles.csv'
merge_columns(input_file, output_file)