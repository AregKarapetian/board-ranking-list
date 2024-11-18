import pandas as pd
import os
import matplotlib.pyplot as plt

# ---- 1. Load Data ----
def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath, low_memory=False)
        print(f"Data loaded successfully from {filepath} with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

# ---- 2. Clean Data ----
def general_clean_data(data):
    """Clean and standardize the dataset."""
    for col in data.select_dtypes(include=['number']).columns:
        data[col] = data[col].fillna(0)
    for col in data.select_dtypes(include=['object']).columns:
        mode_value = data[col].mode().iloc[0] if not data[col].mode().empty else 'Unknown'
        data[col] = data[col].fillna(mode_value)

    # Standardize column names
    data.columns = [col.lower().replace(" ", "_") for col in data.columns]
    data.reset_index(drop=True, inplace=True)
    return data

# ---- 3. Combine Datasets ----
def combine_datasets(data1, data2):
    """Combine two datasets on the 'id' column."""
    combined = pd.merge(data1, data2, on='id', suffixes=('_2020', '_2022'))
    print(f"Combined dataset has {combined.shape[0]} rows and {combined.shape[1]} columns.")
    print(f"Columns in combined dataset: {list(combined.columns)}")
    return combined

# ---- 4. Calculate Bayesian Rating ----
def calculate_bayesian_rating(data, votes_col, average_col, m, C):
    """Calculate Bayesian rating for a dataset."""
    data['bayesian_rating'] = (
        (data[votes_col] / (data[votes_col] + m)) * data[average_col] +
        (m / (data[votes_col] + m)) * C
    )
    return data

# ---- 5. Compare Rankings ----
def compare_with_bgg_ranking(data, bgg_rank_col, bayesian_col):
    """Compare BGG ranking with Bayesian ranking."""
    data_sorted_bgg = data.sort_values(by=bgg_rank_col).head(20)
    data_sorted_bayesian = data.sort_values(by=bayesian_col, ascending=False).head(20)

    print("\nTop 20 by BGG Ranking:")
    print(data_sorted_bgg[['name_2020', bgg_rank_col]])

    print("\nTop 20 by Bayesian Rating:")
    print(data_sorted_bayesian[['name_2020', bayesian_col]])

    return data_sorted_bgg, data_sorted_bayesian

# ---- 6. Visualization ----
def compare_ratings(data, average_col, bayesian_col):
    """Visualize the comparison of raw average and Bayesian ratings."""
    plt.figure(figsize=(10, 6))
    plt.scatter(data[average_col], data[bayesian_col], alpha=0.5)
    plt.xlabel('Raw Average Rating')
    plt.ylabel('Bayesian Rating')
    plt.title('Bayesian Rating vs. Raw Average Rating')
    plt.show()

def visualize_vote_distribution(data, votes_col):
    """Visualize the distribution of votes."""
    plt.figure(figsize=(10, 6))
    data[votes_col].plot(kind='hist', bins=50, edgecolor='k')
    plt.xlabel('Number of Votes')
    plt.title('Distribution of Number of Votes')
    plt.show()

# ---- 7. Save Data ----
def save_data(data, filepath):
    """Save the processed data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data.to_csv(filepath, index=False)
    print(f"Data saved successfully to {filepath}")

# ---- Main Execution ----
if __name__ == "__main__":
    # File paths
    file_2020_path = "datasets/cleaned_data/cleaned_2020-08-19.csv"
    file_2022_path = "datasets/cleaned_data/cleaned_2022-01-08.csv"
    processed_data_path = "datasets/processed_data/combined_ranked.csv"

    # Load datasets
    data_2020 = load_data(file_2020_path)
    data_2022 = load_data(file_2022_path)

    if data_2020 is not None and data_2022 is not None:
        # Clean datasets
        data_2020 = general_clean_data(data_2020)
        data_2022 = general_clean_data(data_2022)

        # Combine datasets
        combined_data = combine_datasets(data_2020, data_2022)

        # Bayesian ranking parameters
        votes_col = 'users_rated_2020'  # Adjust based on actual column name
        average_col = 'average_2020'    # Adjust based on actual column name
        bgg_rank_col = 'rank_2020'      # Adjust based on actual column name

        C = combined_data[average_col].mean()  # Global average rating
        m = combined_data[votes_col].quantile(0.50)  # Median number of votes

        # Calculate Bayesian rating
        combined_data = calculate_bayesian_rating(combined_data, votes_col, average_col, m, C)

        # Compare rankings
        compare_with_bgg_ranking(combined_data, bgg_rank_col, 'bayesian_rating')

        # Visualizations
        compare_ratings(combined_data, average_col, 'bayesian_rating')
        visualize_vote_distribution(combined_data, votes_col)

        # Save processed data
        save_data(combined_data, processed_data_path)
