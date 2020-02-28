import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = os.path.dirname(__file__)
plot_loc = 'disney_movies_gross_plots'
plt.style.use('ggplot')


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


def plot_top5(df):
    """Save a plot of the top 5 total grossed titles"""

    df = df.sort_values('total_gross', ascending=False)
    plt.bar(df[:5]['movie_title'], df[:5]['total_gross'])

    plt.xticks(rotation=30, ha='right')
    plt.title('Top 5 Total Grossing Disney Movies')
    plt.xlabel('Movie Title')
    plt.ylabel('Total Gross ($)')
    plt.tight_layout()

    plt.savefig(f'{path}/{plot_loc}/top5_by_total_gross.png')


if __name__ == '__main__':
    df = pd.read_csv(f'{path}/disney_movies_total_gross.csv')

    # labels
    df_labels = df.columns

    # print(df[:2]['movie_title'])

    gross_to_int(df)
    plot_top5(df)
