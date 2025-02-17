import pandas as pd

def load_data(file_path):
    """Loads the dataset and handles missing values."""
    df = pd.read_csv(file_path)
    
    # Handle missing values by filling with mean
    df.fillna(df.mean(), inplace=True)
    
    return df

def clean_data(df):
    """Performs basic data cleaning."""
    df = df.dropna()  # Remove missing values
    return df

def summarise_data(df):
    """Returns basic summary statistics."""
    return df.describe()

if __name__ == "__main__":
    file_path = "raw_data.csv"
    data = load_data(file_path)
    clean_data = clean_data(data)
    summary = summarise_data(clean_data)
    print(summary)
