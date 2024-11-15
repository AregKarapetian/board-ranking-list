import pandas as pd
import os

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath, low_memory=False)
        print(f"Data loaded successfully from {filepath} with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def general_clean_data(data):
    """
    General-purpose cleaning function that fills missing values with reasonable defaults
    and standardizes column names.
    
    Parameters:
    - data (DataFrame): The dataset to clean.
    
    Returns:
    - DataFrame: The cleaned dataset.
    """
    # 1. Fill missing values
    # For numeric columns, fill missing values with 0 (assuming counts or similar fields)
    for col in data.select_dtypes(include=['number']).columns:
        data[col].fillna(0, inplace=True)
        print(f"Filled missing values in numeric column '{col}' with 0.")

    # For object (text) columns, fill missing values with the mode (most frequent value)
    for col in data.select_dtypes(include=['object']).columns:
        mode_value = data[col].mode().iloc[0] if not data[col].mode().empty else 'Unknown'
        data[col].fillna(mode_value, inplace=True)
        print(f"Filled missing values in text column '{col}' with mode '{mode_value}'.")

    # 2. Standardize column names (optional step)
    # Convert column names to lowercase and replace spaces with underscores
    data.columns = [col.lower().replace(" ", "_") for col in data.columns]
    print("Standardized column names.")

    # 3. Reset index after cleaning
    data.reset_index(drop=True, inplace=True)
    print("Data cleaning complete.")

    return data

def save_data(data, filepath):
    """Save the cleaned data to a new CSV file."""
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Attempt to save the file
        data.to_csv(filepath, index=False)
        print(f"Cleaned data successfully saved to {filepath}.")
    except Exception as e:
        print(f"Failed to save data to {filepath}: {e}")

def main():
    # Define file paths for the raw and cleaned datasets
    raw_data_paths = [
        "datasets/raw_data/2020-08-19.csv",
        "datasets/raw_data/2022-01-08.csv",
        "datasets/raw_data/bgg-15m-reviews.csv",
        "datasets/raw_data/bgg-19m-reviews.csv",
        "datasets/raw_data/games_detailed_info.csv"
    ]
    cleaned_data_paths = [
        "datasets/cleaned_data/cleaned_2020-08-19.csv",
        "datasets/cleaned_data/cleaned_2022-01-08.csv",
        "datasets/cleaned_data/cleaned_bgg-15m-reviews.csv",
        "datasets/cleaned_data/cleaned_bgg-19m-reviews.csv",
        "datasets/cleaned_data/cleaned_games_detailed_info.csv"
    ]

    # Iterate through each dataset, clean, and save
    for raw_path, cleaned_path in zip(raw_data_paths, cleaned_data_paths):
        # Load the data
        data = load_data(raw_path)
        if data is not None:
            # Clean the data using the general cleaning function
            cleaned_data = general_clean_data(data)
            
            # Save the cleaned data
            save_data(cleaned_data, cleaned_path)

if __name__ == "__main__":
    main()
