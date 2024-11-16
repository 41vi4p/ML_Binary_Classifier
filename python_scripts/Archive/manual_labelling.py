import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv('cyber-operations-incidents1.csv')

# Step 2: Initialize an empty list to store labeled data
labeled_data = []

# Step 3: Loop through each row and prompt for a label
for index, row in data.iterrows():
    print(f"\nTitle: {row['Title']}")
    print(f"Description: {row['Description']}")
    print("\nIs this related to cybersecurity or cyberthreats? (1 for Yes, 0 for No)")
    
    # Step 4: Get user input for the label
    label = input("Enter label: ")
    
    # Append the label to the row
    row['Label'] = int(label)
    
    # Add the labeled row to the list
    labeled_data.append(row)

# Step 5: Convert the list to a DataFrame
labeled_df = pd.DataFrame(labeled_data)

# Step 6: Save the labeled data to a new CSV file
labeled_df.to_csv('labeled_cyber_operations_incidents.csv', index=False)

print("Labeled data saved to 'labeled_cyber_operations_incidents.csv'")