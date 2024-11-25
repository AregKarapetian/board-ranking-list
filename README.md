# Board Games Ranking Project

The Board Games Ranking Project is a Python-based tool designed to analyze, rank, and compare board games using the BoardGameGeek dataset. The aim is to produce an alternative ranking based on user preferences, including metrics like ownership, wishes, and trades. The project provides insights into how popularity differs from official BoardGameGeek rankings and visualizes these discrepancies.

## Features

1. Data Processing: Load and clean datasets, ensuring numeric consistency for key columns.
2. Popularity Score Calculation: Compute a custom popularity metric using user-provided interaction data (owned, wishing, wanting, trading).
3. Visualization: Generate graphs comparing BGG rankings with popularity-based rankings.
4. Streamlit Web App: Explore and interact with the data through a web-based dashboard.

## Usage
1. Processing the Dataset
Run the script to clean and calculate popularity scores:
```
python process.py
```
This will:

Load the raw data.
Add a calculated popularity score.
Save the cleaned dataset to datasets/processed_data/games_with_popularity.csv.

2. Visualizing Data
To visualize discrepancies between rankings, run the Streamlit web app:
```
streamlit run .\visualize.py
```
  You can interact with the app to explore rank comparisons.


## File Structure
board-ranking-list/
├── code/
│   ├── data_processing/
│   │   ├── load_clean_data.py        # Load and clean datasets
│   ├── plotting/
│   │   ├── visualize_discrepancies.py # Visualization of rank discrepancies
│   ├── ranking_model/
│       ├── popularity_score.py        # Calculate popularity scores
├── datasets/
│   ├── raw_data/                      # Original datasets
│   ├── processed_data/                # Processed datasets with popularity scores
├── tests/                             # Test scripts
├── venv/                              # Virtual environment folder
├── process.py                         # Main script for data processing
├── visualize.py                       # Main script for visualization
├── .gitignore                         # Files to ignore in Git
├── README.md                          # Project documentation


### Dataset
The project uses the BoardGameGeek dataset, which contains:

Board game rankings, reviews, and user interaction data.
Columns include owned, wishing, wanting, trading, and Board Game Rank.
Download the dataset from Kaggle or other reliable sources.


### Technologies Used

Languages: Python
Libraries: Pandas, NumPy, Matplotlib, Streamlit
Dataset Source: BoardGameGeek



  
