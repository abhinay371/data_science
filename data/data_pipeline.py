import pandas as pd
import os

# Define the file path
file_path = r"C:\Users\Dell\OneDrive\Desktop\datawa\projects\data\raw\bike+sharing+dataset\day.csv"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file at {file_path} does not exist.")

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully.")
except Exception as e:
    raise RuntimeError(f"An error occurred while loading the data: {e}")

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())

# Display the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Save a processed version of the dataset (if needed)
processed_file_path = r"C:\Users\Dell\OneDrive\Desktop\datawa\projects\data\processed\processed_day.csv"
os.makedirs(os.path.dirname(processed_file_path), exist_ok=True)
data.to_csv(processed_file_path, index=False)
print(f"\nProcessed data saved to {processed_file_path}.")