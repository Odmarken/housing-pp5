import pandas as pd

def clean_data(file_path):
    """
    Cleans the dataset by handling missing values and ensuring data validity.

    Args:
        file_path (str): Path to the raw dataset file.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print(f"Dataset loaded from {file_path}. Shape: {df.shape}")

        # Drop rows with missing sale prices
        df = df.dropna(subset=['SalePrice'])

        # Drop unnecessary columns (e.g., 'Id')
        if 'Id' in df.columns:
            df = df.drop(columns=['Id'])

        # Fill missing numerical values with column medians
        df = df.fillna(df.median())

        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
