"""
labels: 'movie_title', 'release_date', 'genre', 'MPAA_rating', 'total_gross',
        'inflation_adjusted_gross'
"""

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
        labels = [key for key in genres]
        values = [genres[key][1] for key in genres]
        wedges, texts = plt.pie(values)

        # drawing lines to wedges to make data easier to read
        kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")
        for i, p in enumerate(wedges):
            angle = (p.theta2 - p.theta1) / 2 + p.theta1
            x = np.cos(np.deg2rad(angle))
            y = np.sin(np.deg2rad(angle))
            horizontalalignment = {-1: 'right', 1: 'left'}[int(np.sign(x))]
            connectionstyle = f'angle,angleA=0,angleB={angle}'
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            plt.annotate(
                f'{labels[i]} - {round(values[i]/total*100, 1)}%', 
                (x,y),
                xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment,
                **kw
            )
        
        plt.title('Disney\'s Genre Values')
        plt.axis('equal')
        plt.tight_layout()
            
        plt.show()


    def best_MPAA_rating(self):
        pass


if __name__ == '__main__':
    disney = Disney_Movies_Gross()
    disney.gross_to_int()
    # disney.plot_top5()

    disney.best_genre()

    # print(disney.df['genre'].unique())
