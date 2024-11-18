import pandas as pd

# File path for the dataset
csv_path = r'C:\Users\Sonali\OneDrive\Desktop\imageprocessing\data\Challenge2 (1).csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(csv_path)

# Display the first few rows for debugging and inspection
print("First few rows of the original data:")
print(df.head())

# Expected number of columns in the dataset (update based on the actual structure of the CSV)
expected_columns = 201

# Filter rows that have the correct number of columns
# The lambda function checks each row's length and ensures it matches the expected number of columns.
cleaned_df = df[df.apply(lambda row: len(row) == expected_columns, axis=1)]

# Reset the index of the cleaned DataFrame to maintain a continuous index
# drop=True ensures the old index is not added as a new column in the DataFrame.
cleaned_df.reset_index(drop=True, inplace=True)

# Save the cleaned data to a new CSV file
cleaned_csv_path = r'C:\Users\Sonali\OneDrive\Desktop\imageprocessing\cleaned_data.csv'
cleaned_df.to_csv(cleaned_csv_path, index=False)

# Print the path where the cleaned data is saved
print(f"Cleaned data saved to: {cleaned_csv_path}")
