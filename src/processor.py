import pandas as pd
import re


def normalize_column_name(name):
    """Normalize API column headers to consistent snake_case names."""
    normalized = str(name).strip().lower()
    normalized = normalized.replace(' ', '_')
    normalized = normalized.replace('/', '_')
    normalized = normalized.replace('-', '_')
    normalized = normalized.replace('%', 'percent')
    return normalized


def shorten_cause(cause):
    """
    Cleans cause descriptions by removing ICD codes in parentheses.
    Example: 'Accidents Except Drug Posioning (V01-X39)' -> 'Accidents Except Drug Posioning'
    """
    if not isinstance(cause, str):
        return cause
        
    # Get everything before the parentheses
    regex_expression = r'(.*)\(.*\)'
    regex = re.compile(regex_expression)
    matches = regex.finditer(cause)
    
    for m in matches:
        return m.group(1).strip()[:30]
    return cause[:30]

def create_dataframe(raw_json):
    """Converts raw JSON data into a Pandas DataFrame and normalizes its columns."""
    columns = [col['name'] for col in raw_json['meta']['view']['columns']]
    normalized_columns = [normalize_column_name(name) for name in columns]
    df = pd.DataFrame(raw_json['data'], columns=normalized_columns)
    return df

def clean_dataframe(df):
    """Applies regex cleaning and converts numeric columns."""
    if 'leading_cause' in df.columns:
        df["cause"] = df["leading_cause"].apply(shorten_cause)
        df = df.drop(columns=['leading_cause'])

    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')

    # Ensure numeric columns are handled properly (ignoring missing '.' values)
    numeric_cols = ['deaths', 'death_rate', 'age_adjusted_death_rate']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    return df