import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath, low_memory=False)
        print(f"Data loaded successfully from {filepath} with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def clean_ranking_column(data, rank_col):
    """
    Ensure the ranking column is numeric by replacing non-numeric values with NaN.
    """
    data[rank_col] = pd.to_numeric(data[rank_col], errors='coerce')
    print(f"Non-numeric values in '{rank_col}' converted to NaN.")
    return data

def calculate_correlation(data, popularity_col, rank_col):
    """
    Calculate Pearson correlation between popularity score and a ranking column.
    """
    # Drop rows with NaN in the relevant columns
    data_cleaned = data.dropna(subset=[popularity_col, rank_col])
    correlation = data_cleaned[[popularity_col, rank_col]].corr().iloc[0, 1]
    print(f"Correlation between {popularity_col} and {rank_col}: {correlation:.4f}")
    return correlation

def identify_discrepancies(data, popularity_col, rank_col, threshold=1000):
    """
    Identify discrepancies between popularity score and rankings.
    """
    # Drop rows with NaN in the rank column
    data_cleaned = data.dropna(subset=[rank_col])

    # Calculate rank difference
    data_cleaned['rank_difference'] = data_cleaned[rank_col] - data_cleaned[popularity_col].rank(ascending=False)
    
    # Identify popular but poorly ranked games
    popular_poorly_ranked = data_cleaned[data_cleaned['rank_difference'] > threshold]
    print(f"Games that are popular but poorly ranked: {len(popular_poorly_ranked)}")
    
    # Identify unpopular but highly ranked games
    unpopular_highly_ranked = data_cleaned[data_cleaned['rank_difference'] < -threshold]
    print(f"Games that are unpopular but highly ranked: {len(unpopular_highly_ranked)}")
    
    return popular_poorly_ranked, unpopular_highly_ranked

if __name__ == "__main__":
    # File path to the dataset
    data_path = "datasets/raw_data/games_detailed_info.csv"  # Update the path as necessary

    # Load dataset
    data = load_data(data_path)

    if data is not None:
        # Column names
        popularity_col = 'popularity_score'  # Ensure this column is calculated
        bayesian_rank_col = 'bayesaverage'   # Update with the correct column name
        bgg_rank_col = 'Board Game Rank'     # Update with the correct column name
        owned_col = 'owned'
        wishing_col = 'wishing'
        wanting_col = 'wanting'
        trading_col = 'trading'

        # Step 1: Calculate Popularity Score
        if popularity_col not in data.columns:
            data['popularity_score'] = data[owned_col] + data[wishing_col] + data[wanting_col] - data[trading_col]
            print("Popularity scores calculated.")

        # Step 2: Clean Ranking Column
        data = clean_ranking_column(data, bgg_rank_col)

        # Step 3: Compute Correlations
        print("\nCorrelation Analysis:")
        calculate_correlation(data, popularity_col, bayesian_rank_col)
        calculate_correlation(data, popularity_col, bgg_rank_col)

        # Step 4: Identify Discrepancies
        print("\nDiscrepancy Analysis:")
        threshold = 1000  # Adjust threshold as needed
        popular_poorly_ranked, unpopular_highly_ranked = identify_discrepancies(data, popularity_col, bgg_rank_col, threshold)

        
