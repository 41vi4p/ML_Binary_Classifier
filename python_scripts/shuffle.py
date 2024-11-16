import pandas as pd
import glob

# Step 1: Define the file paths
file_paths = ['merged.csv', 'OP_balanced.csv']  # Replace with your actual file paths

# Step 2: Load the CSV files into DataFrames
dataframes = [pd.read_csv(file) for file in file_paths]

# Step 3: Concatenate the DataFrames
merged_df = pd.concat(dataframes, ignore_index=True)

# Step 4: Shuffle the rows
shuffled_df = merged_df.sample(frac=1).reset_index(drop=True)

# Step 5: Save the merged and shuffled DataFrame to a new CSV file
shuffled_df.to_csv('merged_shuffled.csv', index=False)

print("Merged and shuffled CSV saved as 'merged_shuffled.csv'")