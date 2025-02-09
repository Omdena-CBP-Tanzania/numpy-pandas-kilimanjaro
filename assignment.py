import numpy as np
import pandas as pd

def create_1d_array():
   
    return np.array([1, 2, 3, 4, 5])

def create_2d_array():
    return np.arange(1, 10).reshape(3, 3)

def array_operations(arr):
    mean_value = np.mean(arr)
    std_dev = np.std(arr)
    max_value = np.max(arr)
    return mean_value, std_dev, max_value

def read_csv_file(filepath):
    try:
        df = pd.read_csv(filepath)
        print("CSV file loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file is not a valid CSV.")
        return None

def handle_missing_values(df):
    print("Missing values per column before handling:\n", df.isnull().sum())

    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("Missing values per column after handling:\n", df.isnull().sum())

    return df

def select_data(df):
    try:
        selected_columns = ['Name', 'Salary']
        df_selected = df[selected_columns]

        df_selected = df_selected.iloc[:3]

        return df_selected
    except KeyError as e:
        print(f"Error: One or more specified columns do not exist in the DataFrame - {e}")
        return None

def rename_columns(df):
    column_mapping = {
        'Name': 'Full Name',
        'Age': 'Age (Years)',
        'Salary': 'Monthly Salary'
    }
    
    df = df.rename(columns=column_mapping)
    
    return df
