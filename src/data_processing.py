import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the insurance dataset from a CSV file.
    """
    df = pd.read_csv(filepath, parse_dates=['TransactionMonth'])
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic preprocessing:
    - Convert categorical columns to category dtype
    - Handle missing values if needed
    """
    # Convert some columns to categorical
    categorical_cols = ['Province', 'VehicleType', 'Gender', 'PostalCode']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # Check and handle missing values
    df = df.dropna(subset=['TotalPremium', 'TotalClaims'])  # Drop rows missing key financial data

    return df
