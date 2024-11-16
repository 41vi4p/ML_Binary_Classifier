import pandas as pd

# Read the news dataset
news_data = pd.read_csv('a9.csv')

# Define keywords to override the label to 0
keywords2 = ['hacked to death', 'tree', 'trees']

# Override the label to 0 if any of the keywords in keywords2 are detected
news_data.loc[news_data['Description'].str.contains('|'.join(keywords2), case=False, na=False), 'Label'] = 0

# Save the dataset with labels to a new CSV file
news_data.to_csv('uko2.csv', index=False)

print("Filtered news articles saved to 'uko.csv'")
