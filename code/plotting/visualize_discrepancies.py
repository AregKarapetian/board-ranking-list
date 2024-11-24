import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# File path to updated dataset
updated_data_path = "datasets/processed_data/games_with_popularity.csv"

@st.cache
def load_data(file_path):
    """
    Load data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None

def visualize():
    st.title("BGG Rank vs. Popularity Rank")

    # Load updated dataset
    data = load_data(updated_data_path)

    if data is not None:
        # Display dataset
        st.header("Dataset with Popularity Scores")
        st.dataframe(data)

        # Add rank comparison
        if 'popularity_score' in data.columns and 'Board Game Rank' in data.columns:
            st.header("Comparison: BGG Rank vs. Popularity Rank")

            # Ensure numeric columns
            data['popularity_rank'] = data['popularity_score'].rank(ascending=False)
            data['Board Game Rank'] = pd.to_numeric(data['Board Game Rank'], errors='coerce')
            data.dropna(subset=['Board Game Rank', 'popularity_rank'], inplace=True)

            # Scatter plot for BGG Rank vs. Popularity Rank
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(data['Board Game Rank'], data['popularity_rank'], alpha=0.5, color='green')
            ax.set_title("BGG Rank vs. Popularity Rank")
            ax.set_xlabel("BGG Rank")
            ax.set_ylabel("Popularity Rank")
            ax.grid(True)
            st.pyplot(fig)
        else:
            st.error("Required columns for comparison are missing.")
