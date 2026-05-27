import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Description'] = df['Description'].str.strip()
    df = df.dropna(subset=['Amount']) # Drop rows where Amount is missing.
    df['Amount'] = df['Amount'].astype(float)
    return df
