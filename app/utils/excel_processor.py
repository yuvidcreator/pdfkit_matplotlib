import pandas as pd

def process_excel(file_path) -> dict:
    """Extract relevant data from the Excel file for the report."""
    
    df = pd.read_excel(file_path)

    # Ensure there are at least two columns
    if df.shape[1] < 2:
        raise ValueError("Excel file must have at least two columns.")

    # Convert first column to labels and second column to numerical values
    labels = df.iloc[:, 0].astype(str).tolist()
    values = df.iloc[:, 1].astype(float).tolist()

    # Convert to dictionary format
    return dict(zip(labels, values))
