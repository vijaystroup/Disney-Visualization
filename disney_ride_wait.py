"""
Input a date of when you want to visit a certain park, and determine the best
route to take of rides.

get general information such as average wait time of the year of a certain ride.
"""


import os
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

path = os.path.dirname(__file__)
df = pd.read_csv(f'{path}/data/splash_mountain.csv')

# clean data
df.dropna(subset=['SPOSTMIN'], inplace=True)
df.drop(df[df['SPOSTMIN'] < 0].index, inplace=True)


df_2019 = df.loc[df['date'].str.contains('2019')]
x = df.mean()['SPOSTMIN']

plt.axes()
plt.bar(df['datetime'], df['SPOSTMIN'])
plt.plot([0, len(df)], [x, x], 'b--')
plt.xticks([0, len(df)], ['1/1/2012', '12/31/2019'])
plt.ylim(0, 200)
plt.xlabel('Time (01/01/2012 - 12/31/2019)')
plt.ylabel('Waiting Time (min)')
plt.title('Wait Times for Splash Mountain')
plt.savefig(f'{path}/disney_ride_wait_reports/splash_mountain.png')
plt.show()
