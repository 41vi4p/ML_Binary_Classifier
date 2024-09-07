import pandas as pd

# Step 1: Read the CSV file
input_file = 'cyber-operations-incidents.csv'
df = pd.read_csv(input_file)

# Step 2: Add a label column with all values set to 1
df['Label'] = 1

# Step 3: Write the updated DataFrame to a new CSV file
output_file = 'labeled_cyber_operations_incidents.csv'
df.to_csv(output_file, index=False)

print(f"Updated CSV file saved as {output_file}")
