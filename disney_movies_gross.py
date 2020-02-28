import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = os.path.dirname(__file__)


def gross_to_int(df):
    """Change datatype of gross values from string to integer for sorting"""

    for i in df.iterrows():
        total_gross = int(
                i[1]['total_gross'].replace('$', '').replace(',', '')
            )
        inflation_adj_gross = int(
                i[1]['inflation_adjusted_gross'].replace('$', '').replace(',', '')
            )
        
        df.replace(
            to_replace = [i[1]['total_gross'], i[1]['inflation_adjusted_gross']],
            value = [total_gross, inflation_adj_gross],
            inplace = True
        )


if __name__ == '__main__':
    df = pd.read_csv(f'{path}/disney_movies_total_gross.csv')

    # labels
    df_labels = df.columns

    gross_to_int(df)
    print(df)