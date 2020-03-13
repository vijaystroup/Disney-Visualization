"""
Input a date of when you want to visit a certain park, and determine the best
route to take of rides.

get general information such as average wait time of the year of a certain ride.
"""

import concurrent.futures
import os
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')
path = os.path.dirname(__file__)
report_dir = 'disney_ride_wait_reports'


class Ride:
    """Class used for getting general information on wait times for a specific
    park
    """

    def __init__(self, df_data_path):
        self._ride = df_data_path
        self.ride = df_data_path.split('_')
        self.ride_cap = []
        for word in self.ride:
            self.ride_cap.append(word.capitalize())
        self.ride = ' '.join(self.ride_cap)

        # set dataframe and clean null values
        self.df = pd.read_csv(f'{path}/data/{df_data_path}.csv')
        self.df.dropna(subset=['SPOSTMIN'], inplace=True)
        self.df.drop(self.df[self.df['SPOSTMIN'] < 0].index, inplace=True)

    def master_plot(self):
        """Method for plotting wait times from 2012 to 2019 (the whole dataset)
        """

        mean = self.df._get_numeric_data().mean()['SPOSTMIN']

        plt.bar(self.df['datetime'], self.df['SPOSTMIN'])
        plt.plot([0, len(self.df)], [mean, mean], 'b--')
        plt.xticks([0, len(self.df)], ['1/1/2012', '12/31/2019'])
        plt.ylim(0, self.df.max()['SPOSTMIN'])
        plt.xlabel('Date')
        plt.ylabel('Waiting Time (min)')
        plt.title(f'Wait Times for {self.ride}')
        try:
            plt.savefig(f'{path}/{report_dir}/{self._ride}/master_wait_times.png')
        except Exception:
            os.mkdir(f'{path}/{report_dir}/{self._ride}')
            plt.savefig(f'{path}/{report_dir}/{self._ride}/master_wait_times.png')

    def yearly_plot(self, year):
        """Method for plotting the wait times of each year independently from
        2012 to 2019
        """

        plt.clf()
        df_year = self.df.loc[self.df['date'].str.contains(year)]
        mean = df_year._get_numeric_data().mean()['SPOSTMIN']

        plt.bar(df_year['datetime'], df_year['SPOSTMIN'])
        plt.plot([0, len(df_year)], [mean, mean], 'b--')
        plt.xticks([0, len(df_year)], ['January', 'December'])
        plt.ylim(0, df_year.max()['SPOSTMIN'])
        plt.xlabel('Date')
        plt.ylabel('Waiting Time (min)')
        plt.title(f'{year} Wait Times for {self.ride}')
        try:
            plt.savefig(f'{path}/{report_dir}/{self._ride}/{year}_wait_times.png')
        except Exception:
            os.mkdir(f'{path}/{report_dir}/{self._ride}')
            plt.savefig(f'{path}/{report_dir}/{self._ride}/{year}_wait_times.png')

    def monthly_plot(self, month):
        """Method for plotting wait times for each month in a given year. For
        simplicity as this is only a test program, only the 2019 year will be
        used
        """
        
        plt.clf()

        df_month = self.df.loc[self.df['date'].str.contains(f'{month}/.*/2019')]
        mean = df_month._get_numeric_data().mean()['SPOSTMIN']

        plt.plot(df_month['datetime'], df_month['SPOSTMIN'])
        plt.plot([0, len(df_month)], [mean, mean], 'b--')
        plt.xticks([0, len(df_month)], [f'{month}/01/2019', f'{month}/31/2019'])
        plt.ylim(0, df_month.max()['SPOSTMIN'])
        plt.xlabel('Date')
        plt.ylabel('Waiting Time (min)')
        plt.title(f'{month}/2019 Wait Times for {self.ride}')
        try:
            plt.savefig(f'{path}/{report_dir}/{self._ride}/2019-{month}_wait_times.png')
        except Exception:
            os.mkdir(f'{path}/{report_dir}/{self._ride}')
            plt.savefig(f'{path}/{report_dir}/{self._ride}/2019-{month}_wait_times.png')

    def weekly_plot(self):
        """Method for plotting wait times for each week in a month in a given
        year. For simplicity as this is only a test program, only the month
        January in 2019 year will be used
        """

        pass

    def daily_plot(self):
        """Method for plotting wait times for each day in a week for a month in
        a given year. For simplicity as this is only a test program, only the
        day Saturday in the month January in 2019 year will be used
        """

        pass

    def multi_process(self, plot_type):
        """Method for accelerating the plotting processes using 
        multi-processing
        """

        years = [
            '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'
        ]
        months = [
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'
        ]

        with concurrent.futures.ProcessPoolExecutor() as executor:
            if plot_type == 'yearly_plot':
                executor.map(self.yearly_plot, years)
            elif plot_type == 'monthly_plot':
                executor.map(self.monthly_plot, months)


def best_route():
    """Function that will decided the best route to take in a certain park on a
    certain day
    """

    pass


if __name__ == '__main__':
    ride_splash = Ride('splash_mountain')
    # ride_splash.master_plot()
    # ride_splash.multi_process('yearly_plot')
    ride_splash.multi_process('monthly_plot')
