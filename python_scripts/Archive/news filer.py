import pandas as pd

# Read the news dataset
news_data = pd.read_csv('News_Articles_Indian_Express.csv')

# Define cybersecurity-related keywords
keywords = ['cybersecurity', 'hacking', 'malware', 'cybercrime', 'security breach', 'hackers', 'hacked']

# Filter out news articles that contain cybersecurity-related keywords
news_data_filtered = news_data[news_data['text'].str.contains('|'.join(keywords), case=False, na=False)]

# Save the filtered news articles to a new CSV file
news_data_filtered.to_csv('filtered_news.csv', index=False)

print("Filtered news articles saved to 'filtered_news.csv'")