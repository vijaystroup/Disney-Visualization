import math
import os
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

path = os.path.dirname(__file__)
df = pd.read_csv(f'{path}/data/splash_mountain.csv')

# clean data
df.drop(df[df['SPOSTMIN'] < 0].index, inplace=True)
df.dropna(subset=['SPOSTMIN'], inplace=True)


df_2019 = df.loc[df['date'].str.contains('2019')]

plt.plot(df[:10]['datetime'], df[:10]['SPOSTMIN'])
plt.show()