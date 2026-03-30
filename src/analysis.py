import pandas as pd
import numpy as np

def generate_death_pivot(df):
    """
    Creates a pivot table to compute the average deaths by cause, 
    separated by sex and race/ethnicity.
    """
    pivot = pd.pivot_table(
        df,
        values='deaths',
        index=['cause'],                    # rows
        columns=['sex', 'race_ethnicity'],  # columns
        aggfunc=np.mean                     # aggregation function
    )
    return pivot

def generate_death_rate_pivot(df):
    """
    Change the pivot_table to compute the average `age_adjusted_death_rate` 
    instead of the sum of deaths, as requested in the notebook exercises.
    """
    if 'age_adjusted_death_rate' not in df.columns:
        return None
        
    pivot = pd.pivot_table(
        df,
        values='age_adjusted_death_rate',
        index=['cause'],
        columns=['sex', 'race_ethnicity'],
        aggfunc=np.mean
    )
    return pivot