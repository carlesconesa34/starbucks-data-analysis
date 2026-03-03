"""
Starbucks Data Cleaning
Author: Carles Conesa
Dataset: Starbucks Customer Ordering Patterns (100k transactions)
Description: This script cleans the raw dataset.
"""

import pandas as pd

import os

from starbucks_exploration import load_dataset


def modify_variable_types(df):
    """
    Modifies date and time variables.
    """
    # Standardizing date and time
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_time'] = pd.to_datetime(df['order_time'], format='%H:%M').dt.time
    
    return df


if __name__ == "__main__":
    test_path = "data/raw/starbucks_customer_ordering_patterns.csv"
    output_path = "data/processed/starbucks_customer_ordering_patterns_cleaned.csv"
    
    print("\nStarting test...\n")
    
    df_test = load_dataset(test_path)
    
    if df_test is not None:
        df_test = modify_variable_types(df_test)
        
        os.makedirs('data/processed', exist_ok=True)
        df_test.to_csv(output_path, index=False)
        
        print("\nTest ended.\n")
    else:
        print("\nTest failed: unexpected error while loading the dataset.\n")