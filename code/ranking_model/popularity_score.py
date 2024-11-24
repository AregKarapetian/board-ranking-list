import pandas as pd
import numpy as np
import sys

sys.path.append('code/data_processing')
from load_clean_data import LoaderAndCleaner

def calculate_correlation(data, popularity_col, rank_col):
    """
    Calculate Pearson correlation between popularity score and a ranking column.
    """
    data_cleaned = data.dropna(subset=[popularity_col, rank_col])
    correlation = data_cleaned[[popularity_col, rank_col]].corr().iloc[0, 1]
    print(f"Correlation between {popularity_col} and {rank_col}: {correlation:.4f}")
    return correlation

def add_popularity_score(data, owned_col, wishing_col, wanting_col, trading_col):
    """
    Add a popularity score column to the dataset.
    """
    if all(col in data.columns for col in [owned_col, wishing_col, wanting_col, trading_col]):
        data['popularity_score'] = data[owned_col] + data[wishing_col] + data[wanting_col] - data[trading_col]
        print("Popularity scores calculated.")
    else:
        print("One or more required columns are missing.")
    return data

def save_updated_dataset(data, file_path):
    """
    Save the dataset with popularity scores.
    """
    data.to_csv(file_path, index=False)
    print(f"Dataset with popularity scores saved to {file_path}")

def process():
    # File path to the dataset
    data_path = "datasets/raw_data/games_detailed_info.csv"
    updated_data_path = "datasets/processed_data/games_with_popularity.csv"

    # Create an instance of LoaderAndCleaner
    data_loader = LoaderAndCleaner()

    # Load dataset
    data = data_loader.load_data(data_path)

    if data is not None:
        # Column names
        owned_col = 'owned'
        wishing_col = 'wishing'
        wanting_col = 'wanting'
        trading_col = 'trading'
        bgg_rank_col = 'Board Game Rank'

        # Step 1: Add Popularity Score
        data = add_popularity_score(data, owned_col, wishing_col, wanting_col, trading_col)

        # Step 2: Save the updated dataset
        save_updated_dataset(data, updated_data_path)
