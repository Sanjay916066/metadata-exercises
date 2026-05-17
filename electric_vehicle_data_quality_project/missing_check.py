import pandas as pd

def get_output_schema():
    return pd.DataFrame({
        'Missing_Check': prep_string()
    })

def run(df):
    df['Missing_Check'] = df.isnull().sum(axis=1).astype(str)
    return df