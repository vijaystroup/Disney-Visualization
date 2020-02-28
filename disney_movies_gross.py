"""
labels: 'movie_title', 'release_date', 'genre', 'MPAA_rating', 'total_gross',
        'inflation_adjusted_gross'
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('ggplot')


class Disney_Movies_Gross:
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.plot_loc = 'disney_movies_gross_plots'
        self.df = pd.read_csv(f'{self.path}/disney_movies_total_gross.csv')

    def gross_to_int(self):
        """Change datatype of gross values from string to integer for sorting"""

        for i in self.df.iterrows():
            total_gross = int(
                    i[1]['total_gross'].replace('$', '').replace(',', '')
                )
            inflation_adj_gross = int(
                    i[1]['inflation_adjusted_gross'].replace('$', '').replace(',', '')
                )

            self.df.replace(
                to_replace = [i[1]['total_gross'], i[1]['inflation_adjusted_gross']],
                value = [total_gross, inflation_adj_gross],
                inplace = True
            )
    
    def plot_top5(self):
        """Save a plot of the top 5 total grossed titles"""

        df = self.df.sort_values('total_gross', ascending=False)
        plt.bar(df[:5]['movie_title'], df[:5]['total_gross'])

        plt.xticks(rotation=30, ha='right')
        plt.title('Top 5 Total Grossing Disney Movies')
        plt.xlabel('Movie Title')
        plt.ylabel('Total Gross ($)')
        plt.tight_layout()

        plt.savefig(f'{self.path}/{self.plot_loc}/top5_by_total_gross.png')

    def best_genre(self):
        pass


    def best_MPAA_rating(self):
        pass


if __name__ == '__main__':
    disney = Disney_Movies_Gross()
    disney.gross_to_int()
    disney.plot_top5()

    print(disney.df['genre'].unique())
