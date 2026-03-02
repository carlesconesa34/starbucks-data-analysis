import pandas as pd
pd.set_option("display.max_columns", None)

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def show_dataset_info(df):
    print("\n=== Dataset information===\n")
    df.info()
    print(f"\nDimensions: {df.shape[0]} rows and {df.shape[1]} columns.")

def check_dataset_duplicates(df):
    print("\n=== Dataset duplicates===\n")
    duplicates = df.duplicated().sum()
    print(f"Detected duplicates: {duplicates}")

def check_dataset_nulls(df):
    print("\n=== Dataset nulls===\n")
    nulls = df.isnull().sum()
    print("Null values per column:")
    if nulls.sum() > 0:
        print(nulls[nulls > 0])
    else:
        print("No nulls detected.")

def show_dataset_statistics(df):
    print("\n=== Key statistics===\n")
    
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