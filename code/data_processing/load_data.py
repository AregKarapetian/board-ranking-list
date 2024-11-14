import pandas as pd
import os

# Define file paths
GAMES_DETAILED_INFO = "datasets/raw_data/games_detailed_info.csv"
user_ids_2020 = "datasets/raw_data/2020-08-19.csv"
user_ids_2022 = "datasets/raw_data/2022-01-08.csv"
bgg_reviews_15 = "datasets/raw_data/bgg-15m-reviews.csv"
bgg_reviews_19 = "datasets/raw_data/bgg-19m-reviews.csv"

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None



def main():
    # Load and check each dataset
    games_detailed_info_data = load_data("datasets/raw_data/games_detailed_info.csv")
    if games_detailed_info_data is not None:
        print(f"Total number of games from games_detailed_info.csv: {len(games_detailed_info_data)}")

    user_ids_2020_data = load_data("datasets/raw_data/2020-08-19.csv")
    if user_ids_2020_data is not None:
        print(f"Total number of entries from 2020-08-19.csv: {len(user_ids_2020_data)}")

    user_ids_2022_data = load_data("datasets/raw_data/2022-01-08.csv")
    if user_ids_2022_data is not None:
        print(f"Total number of entries from 2022-01-08.csv: {len(user_ids_2022_data)}")

    bgg_reviews_15_data = load_data("datasets/raw_data/bgg-15m-reviews.csv")
    if bgg_reviews_15_data is not None:
        print(f"Total number of reviews from bgg-15m-reviews.csv: {len(bgg_reviews_15_data)}")

    bgg_reviews_19_data = load_data("datasets/raw_data/bgg-19m-reviews.csv")
    if bgg_reviews_19_data is not None:
        print(f"Total number of reviews from bgg-19m-reviews.csv: {len(bgg_reviews_19_data)}")

if __name__ == "__main__":
    main()