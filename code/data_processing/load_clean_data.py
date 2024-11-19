import pandas as pd
import os

class LoaderAndCleaner:
    def __init__(self):
        pass

    # ---- 1. Load Data ----
    def load_data(self, filepath):
        """
        Load the dataset from a CSV file.

        Parameters:
        - filepath (str): Path to the CSV file.

        Returns:
        - pd.DataFrame: Loaded DataFrame.
        """
        try:
            data = pd.read_csv(filepath, low_memory=False)
            print(f"Data loaded successfully from {filepath} with {data.shape[0]} rows and {data.shape[1]} columns.")
            return data
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None

    # ---- 2. Clean Ranking Column ----
    def clean_ranking_column(self, data, rank_col):
        """
        Ensure the ranking column is numeric by replacing non-numeric values with NaN.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the ranking column.
        - rank_col (str): The name of the ranking column to clean.

        Returns:
        - pd.DataFrame: Updated DataFrame with cleaned ranking column.
        """
        data[rank_col] = pd.to_numeric(data[rank_col], errors='coerce')
        print(f"Non-numeric values in '{rank_col}' converted to NaN.")
        return data

    # ---- 3. Save Cleaned Data ----
    def save_cleaned_data(self, data, filepath):
        """
        Save the cleaned data to a CSV file.

        Parameters:
        - data (pd.DataFrame): DataFrame to save.
        - filepath (str): Path to save the cleaned data.

        Returns:
        - None
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data.to_csv(filepath, index=False)
        print(f"Cleaned data saved successfully to {filepath}")
