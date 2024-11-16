import pandas as pd

def label_news_articles(input_file, output_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Print column names to debug
    print("Column names:", df.columns)

    # Define cybersecurity-related keywords
    keywords = ['cybersecurity', 'hacking', 'malware', 'cybercrime', 'security breach', 'cyber threat', 'cyber attack', 'cyber']

    # Step 2: Add a label column based on the presence of keywords
    df['Label'] = df['Description'].str.contains('|'.join(keywords), case=False, na=False).astype(int)

    # Filter and print only the articles with the keywords
    filtered_df = df[df['Label'] == 1]
    print("Articles with keywords:", filtered_df[['Description', 'Label']])

    # Keep only the specified columns
    #df = df[['id', 'webTitle', 'bodyContent', 'Label']]
    df = df[['Description', 'Label']]
    # Step 3: Write the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Updated CSV file saved as {output_file}")



def merge_columns(input_file, output_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Print column names to debug
    print("Column names:", df.columns)

    # Step 2: Merge the columns into a single 'Description' column
    #df['Description'] = df['Headline'].fillna('') + ' ' + df['Description'].fillna('') + ' ' + df['Article text'].fillna('')
    df['Description'] = df['title'].fillna('') + ' ' + df['content'].fillna('')

    # Step 3: Drop the original columns
    df = df.drop(columns=['id'])

    # Step 4: Write the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Updated CSV file saved as {output_file}")

# Example usage
input_file = '3.csv'
output_file = 'merged_news_articles.csv'
merge_columns(input_file, output_file)


# Example usage
input_file = 'merged_news_articles.csv'
output_file = 'labeled_news_articles.csv'
label_news_articles(input_file, output_file)