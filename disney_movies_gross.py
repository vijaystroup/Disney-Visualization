"""
labels: 'movie_title', 'release_date', 'genre', 'MPAA_rating', 'total_gross',
        'inflation_adjusted_gross'
"""

from collections import OrderedDict
import os
import numpy as np
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

        for row in self.df.iterrows():
            total_gross = int(
                row[1]['total_gross'].replace('$', '').replace(',', '')
            )
            inflation_adj_gross = int(
                row[1]['inflation_adjusted_gross'].replace('$', '').replace(',', '')
            )

            self.df.replace(
                to_replace = [row[1]['total_gross'], row[1]['inflation_adjusted_gross']],
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
        """Method to find out Disney's best selling genre of film"""

        genres = {}
        total = 0
        for row in self.df.iterrows():
            try:
                genre = genres[row[1]['genre']]
                genres.update(
                    {row[1]['genre']: (genre[0]+1, genre[1]+row[1]['inflation_adjusted_gross'])}
                )
                total += row[1]['inflation_adjusted_gross']
            except KeyError:
                genres.update(
                    {row[1]['genre']: (1, row[1]['inflation_adjusted_gross'])}
                )
                total += row[1]['inflation_adjusted_gross']

        # instead of just finding the most money a genre has made, I will compare
        # the value of the genre based upon its gross earnings to how many titles
        # in that genre were produced (mean per title in genre)
        for key in genres:
            max_value = ('', 0)
            value = (key, genres[key][1] / genres[key][0])
            if value[1] > max_value[1]:
                max_value = value

        # plotting data
        labels = [f'{key} - {round(genres[key][1] / total * 100, 1)}%' for key in genres]
        values = [genres[key][1] for key in genres]
            
        colors = ['yellowgreen','red','gold','lightskyblue','black','lightcoral',
                  'blue','pink', 'darkgreen','yellow','grey','violet','magenta',
                  'cyan','grey']
        circle = plt.Circle((0, 0), 0.7, color='white')
        wedges, texts = plt.pie(values, colors=colors)
        p = plt.gcf()
        p.gca().add_artist(circle)

        wedges, labels = self.sort_labels(wedges, labels, values)
        plt.legend(wedges, labels, loc='center', fontsize=8)

        plt.title('Disney\'s Genre Percent Value')
        plt.axis('equal')
        plt.tight_layout()

        plt.savefig(f'{self.path}/{self.plot_loc}/genre_percent_value.png')


    def best_MPAA_rating(self):
        pass

    @staticmethod
    def sort_labels(classes, labels, y):
        """Method of sorting lables for legend. Algorithm from Saullo G. P. Castro
        on StackOverflow."""
        classes, labels, _ = zip(*sorted(
            zip(classes, labels, y),
            key = lambda x: x[2],
            reverse=True
        ))

        return (classes, labels)


if __name__ == '__main__':
    disney = Disney_Movies_Gross()
    disney.gross_to_int()
    # disney.plot_top5()

    disney.best_genre()

    # print(disney.df['genre'].unique())
