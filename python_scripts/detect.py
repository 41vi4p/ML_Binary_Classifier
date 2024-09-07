import pandas as pd

def count_label_1_entries(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Check if the 'Label' column exists
    if 'Label' not in df.columns:
        raise ValueError("The CSV file does not contain a 'Label' column.")
    
    # Count the number of entries with label 1
    count_label_1 = df[df['Label'] == 1].shape[0]
    
    return count_label_1

def count_label_0_entries(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Check if the 'Label' column exists
    if 'Label' not in df.columns:
        raise ValueError("The CSV file does not contain a 'Label' column.")
    
    # Count the number of entries with label 0
    count_label_0 = df[df['Label'] == 0].shape[0]
    
    return count_label_0

# Example usage
csv_file_paths = ['best2.csv']  # List of CSV file paths
for file_path in csv_file_paths:
    count_1 = count_label_1_entries(file_path)
    print(f"File: {file_path}")
    print(f"Number of entries with label 1: {count_1}\n")
    
    count_0 = count_label_0_entries(file_path)
    print(f"Number of entries with label 0: {count_0}\n")
    
    print("---------------------------------------------------")