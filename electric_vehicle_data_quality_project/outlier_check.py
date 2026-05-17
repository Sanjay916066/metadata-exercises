import pandas as pd

def get_output_schema():
    return pd.DataFrame({
        'Outlier_Flag': prep_string()
    })

def run(df):

    col = [c for c in df.columns if 'Electric Range' in c][0]

    mean = df[col].mean()
    std = df[col].std()

    df['Outlier_Flag'] = df[col].apply(
        lambda x: 'Outlier'
        if abs(x - mean) > 2 * std
        else 'Normal'
    )

    return df[['Outlier_Flag']]