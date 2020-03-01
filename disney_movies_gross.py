"""
This module looks at The Walt Disney Company's movie data that will utilize
the movie titles, genre, rating, and inflated adjusted gross. Then we can see
the value of each genre and rating.
"""

import os
from statistics import median, pstdev
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')


class Disney_Movies_Gross:
    """This class has functions to find the best genre and rating for Disney
    to sell the most movies"""
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.plot_loc = 'disney_movies_gross_plots'
        self.df = pd.read_csv(f'{self.path}/data/disney_movies_total_gross.csv')

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

        df = self.df.sort_values('inflation_adjusted_gross', ascending=False)
        plt.bar(df[:5]['movie_title'], df[:5]['inflation_adjusted_gross'])

        # stats
        self.stats('bar', list(df[:5]['inflation_adjusted_gross']))

        plt.xticks(rotation=30, ha='right')
        plt.title('Top 5 Total Grossing Disney Movies')
        plt.xlabel('Movie Title')
        plt.ylabel('Total Gross ($)')
        plt.tight_layout()

        plt.savefig(f'{self.path}/{self.plot_loc}/top5_by_total_gross.png')

    def best_genre(self):
        """Method to find out Disney's best selling genre of film. The value of
        a genre is determined by the mean inflation_adjusted_gross of each
        genre."""

        genres, total, labels, values = self.iter_data('genre', 'inflation_adjusted_gross')

        # plotting data
        colors = ['yellowgreen','red','gold','lightskyblue','black','lightcoral',
                  'blue','pink', 'darkgreen','yellow','grey','violet','magenta',
                  'cyan','grey']
        title = 'Disney\'s Genre Percent Value of Gross Income'
        saveas = 'genre_percent_value'

        self.pie_plot(values, labels, colors, title, saveas)

    def best_MPAA_rating(self):
        """Method for finding the best selling set of titles with a certain
        rating. Just like best_genre, we will get the mean of a title in each
        rating so we can see the real value of each rating"""

        rating, total, labels, values = self.iter_data('MPAA_rating', 'inflation_adjusted_gross')
        
        # plotting data
        colors = ['yellowgreen','red','gold','lightskyblue','black','lightcoral']
        title = 'Disney\'s MPAA Rating Percent Value of Gross Income'
        saveas = 'rating_percent_value'

        self.pie_plot(values, labels, colors, title, saveas)

    def iter_data(self, key, value):
        """Method for getting appropriate data from data file"""

        total = 0
        data = {}
        for row in self.df.iterrows():
            try:
                datum = data[row[1][key]]
                data.update(
                    {row[1][key]: (datum[0]+1, datum[1]+row[1][value])}
                )
                total += row[1][value]
            except KeyError:
                data.update(
                    {row[1][key]: (1, row[1][value])}
                )
                total += row[1][value]
        
        labels = [f'{k} - {round(data[k][1] / total * 100, 1)}%' for k in data]
        values = [data[k][1] for k in data]

        return (data, total, labels, values)

    def pie_plot(self, values, labels, colors, title, saveas):
        """Method for plotting pie charts"""

        circle = plt.Circle((0, 0), 0.7, color='white')
        wedges, texts = plt.pie(values, colors=colors)
        p = plt.gcf()
        p.gca().add_artist(circle)

        wedges, labels = self.sort_labels(wedges, labels, values)
        
        # statistic information
        self.stats('pie', values)

        plt.legend(wedges, labels, loc='center', frameon=False, fontsize=7)

        plt.title(title)
        plt.axis('equal')
        plt.tight_layout()

        plt.savefig(f'{self.path}/{self.plot_loc}/{saveas}.png')

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
    
    @staticmethod
    def stats(plt_type, values):
        """Plotting statistical information on plots: mean, median, std. dev.,
        min, max, total"""

        fontsize = 7
        total = sum(values)
        text = (
            f'Total: ${total}\n'
            f'Mean: ${total / len(values)}\n'
            f'Median: ${median(values)}\n'
            f'Std. Dev.: ${round(pstdev(values), 2)}\n'
            f'Minumum: ${min(values)}   '
            f'\n    z: {round((min(values)-total / len(values)) / pstdev(values), 2)}\n'
            f'Maximum: ${max(values)}   '
            f'\n    z: {round((max(values)-total / len(values)) / pstdev(values), 2)}'
        )

        if plt_type is 'pie':
            plt.text(0.8, 0.6, text, fontsize=fontsize)
        elif plt_type is 'bar':
            plt.text(-3.0, -0.5, text, fontsize=fontsize)


if __name__ == '__main__':
    disney = Disney_Movies_Gross()
    disney.gross_to_int()

    disney.plot_top5()
    plt.clf() # clear top5 plot for best_genre plot
    disney.best_genre()
    plt.clf()
    disney.best_MPAA_rating()
