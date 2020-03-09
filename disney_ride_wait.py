import os
import matplotlib.pyplot as plt
import pandas as pd

path = os.path.dirname(__file__)
df = pd.read_csv(f'{path}/data/splash_mountain.csv')
df.drop(df[df['SPOSTMIN'] < 0].index, inplace=True)
df_2019 = df.loc[df['date'].str.contains('2019')]
print()
print(df_2019)

plt.plot(df[:50]['datetime'], df[:50]['SPOSTMIN'])
plt.show()