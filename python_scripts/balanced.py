import pandas as pd

def create_balanced_dataset(input_csv_file_paths, final_output_csv_file_path):
    balanced_dfs = []

    for input_csv_file_path in input_csv_file_paths:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(input_csv_file_path)
        
        # Check if the 'Label' column exists
        if 'Label' not in df.columns:
            raise ValueError(f"The CSV file {input_csv_file_path} does not contain a 'Label' column.")
        
        # Count the number of entries for each label
        label_counts = df['Label'].value_counts()
        
        # Determine the minimum count among the labels
        min_count = label_counts.min()
        
        # Sample the same number of entries for each label
        balanced_df = pd.concat([
            df[df['Label'] == label].sample(min_count, random_state=42)
            for label in label_counts.index
        ])
        
        # Shuffle the rows of the new DataFrame
        balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)
        
        # Append the balanced DataFrame to the list
        balanced_dfs.append(balanced_df)
        print(f"Balanced dataset created for {input_csv_file_path}")

    # Concatenate all balanced DataFrames
    combined_df = pd.concat(balanced_dfs, ignore_index=True)
    
    # Shuffle the combined DataFrame
    combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Save the combined and shuffled DataFrame to a new CSV file
    combined_df.to_csv(final_output_csv_file_path, index=False)
    print(f"Combined and shuffled dataset saved to {final_output_csv_file_path}")

# Example usage
input_csv_file_paths = ['best2.csv']
final_output_csv_file_path = 'OP_balanced.csv'
create_balanced_dataset(input_csv_file_paths, final_output_csv_file_path)