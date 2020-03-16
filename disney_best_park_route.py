import os
import numpy as np
import pandas as pd

path = os.path.dirname(__file__)


def check_input(checking, lower_limit, upper_limit):
    """Check if the inputs are valid"""

    try:
        checking = int(checking)
        if checking < lower_limit or checking > upper_limit:
            raise Exception
        return checking
    except Exception:
        print('Invalid input, try again.\n')
        best_route(parks)


def nonzero_min(means):
    """Return the minimum value of a list that is non-zero"""

    return np.nanmin(means)


def best_route(parks):
    """Function that will decided the best route to take in a certain park on a
    certain day
    """

    WALK_TIME = 15 # time to walk between rides

    # transform parks dict keys to make it eaiser to match to input
    park_keys = [1, 2, 3, 4, 5]
    parks = dict(zip(park_keys, list(parks.values())))

    park_n = input(
        'Magic Kingdom(1) | Hollywood Studios(2) | Animal Kingdom(3) | '
        'Disneyland(4) | Epcot(5)'
        '\nWhich park would you like to visit?(1-5): '
    )
    park_n = check_input(park_n, 1, 5)
    date = input(
        'Jan(1) | Feb(2) | March(3) | April(4) | May(5) | June(6) | July(7) | '
        'Aug(8) | Sep(9) | Oct(10) | Nov(11) | Dec(12)'
        f'\nWhen would you like to visit park {park_n}?(1-12): '
    )
    date = check_input(date, 1, 12)

    # create dict with key as `variable name` and values as dataframe objects
    rides = {}
    for park in parks[park_n]:
        if park_n == 1: # Magic Kingdom with only 1 ride in dataset
            df_temp = pd.read_csv(f'{path}/data/{parks[park_n]}.csv')
            rides.update(
                {f'df_{parks[park_n]}': df_temp.loc[df_temp['date'].str.contains(f'{date:02}/.*/.*')]}
            )
            break
        else:
            df_temp = pd.read_csv(f'{path}/data/{park}.csv')
            rides.update(
                {f'df_{park}': df_temp.loc[df_temp['date'].str.contains(f'{date:02}/.*/.*')]}
            )

    # clean dataframes
    for dataframe in rides.values():
        dataframe.dropna(subset=['SPOSTMIN'], inplace=True)
        dataframe.drop(dataframe[dataframe['SPOSTMIN'] < 0].index, inplace=True)

    # creating a dict of rides and their mean wait times per day
    ride_means = {}
    ride_keys = list(rides.keys())
    for i, df in enumerate(rides.values()):
        day_means = []
        for day in range(1, 32):
            df_day = df.loc[df['date'].str.contains(f'{date:02}/{day:02}/.*')]
            day_mean = df_day._get_numeric_data().mean()['SPOSTMIN']
            day_means.append(day_mean)
        
        ride_means.update({ride_keys[i]: day_means})

    # dict of total wait times of all rides on a certain day
    first_day = True
    day_mean_totals = {}
    inital_days = True
    nan_mean = 0
    for mean_set in ride_means.values():
        for day in range(0, 31):
            if inital_days:
                if pd.isna(mean_set[day]):
                    day_mean_totals.update({day+1: mean_set[day]})
                else:
                    day_mean_totals.update({day+1: mean_set[day]})
            else:
                if pd.isna(mean_set[day]):
                    day_mean_totals.update({day+1: day_mean_totals[day+1] + mean_set[day]})
                else:
                    day_mean_totals.update(
                        {day+1: day_mean_totals[day+1] + mean_set[day]}
                    )

        inital_days = False

    # get the best day to visit the park
    min_mean = nonzero_min(list(day_mean_totals.values()))
    for key, value in day_mean_totals.items(): 
        if min_mean == value: 
            best_day = key

    print(best_day)



if __name__ == '__main__':
    parks = {
        'Magic Kingdom': ('7_dwarfs_train'),
        'Hollywood Studios':
            ('alien_saucers', 'rock_n_rollercoaster', 'slinky_dog', 'toy_story_mania'),
        'Animal Kingdom':
            ('dinosaur', 'expedition_everest', 'flight_of_passage', 
             'kilimanjaro_safaris', 'navi_river'),
        'Disneyland': ('pirates_of_caribbean', 'splash_mountain'),
        'Epcot': ('soarin', 'spaceship_earth')
    }

    best_route(parks)