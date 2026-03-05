"""
Starbucks Data Exploration
Author: Carles Conesa
Dataset: Starbucks Customer Ordering Patterns (100k transactions)
Description: This script explores the raw dataset.
"""

import pandas as pd

pd.set_option("display.max_columns", None)


def load_dataset(file_path):
    """
    Attempts to load and provide a preview of the dataset.
    
    Args:
        file_path (str): The path to the CSV file to explore.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print(df.head())
        return df
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def show_dataset_info(df):
    """Displays the technical metadata of the DataFrame (types, memory usage)."""
    print("\n=== Dataset information===")
    df.info()
    print(f"\nDimensions: {df.shape[0]} rows and {df.shape[1]} columns.")


def check_dataset_duplicates(df):
    """Calculates the total number of duplicate rows in the dataset."""
    print("\n=== Dataset duplicates===")
    duplicates = df.duplicated().sum()
    print(f"Detected duplicates: {duplicates}")


def check_dataset_nulls(df):
    """Identifies and prints columns containing missing (null) values."""
    print("\n=== Dataset nulls===")
    nulls = df.isnull().sum()
    print("Null values per column:")
    if nulls.sum() > 0:
        print(nulls[nulls > 0])
    else:
        print("No nulls detected.")


def show_dataset_statistics(df):
    """Generates descriptive statistics for key business metrics."""
    print("\n=== Key statistics===")
    key_columns = ['total_spend', 'fulfillment_time_min', 'customer_satisfaction']
    valid_columns = []
    
    for col in key_columns:
        if col in df.columns:
            valid_columns.append(col)

    if len(valid_columns) > 0:
        print(df[valid_columns].describe().round(2))
    else:
        print("No key columns found.")


if __name__ == "__main__":
    test_path = "data/raw/starbucks_customer_ordering_patterns.csv"
    
    print("\nStarting test...\n")
    
    
    df_test = load_dataset(test_path)
    
    if df_test is not None:
        show_dataset_info(df_test)
        
        check_dataset_duplicates(df_test)
        
        check_dataset_nulls(df_test)
        
        show_dataset_statistics(df_test)
        
        print("\nTest ended.\n")
    else:
        print("\nTest failed: unexpected error while loading the dataset.\n")