import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]
data['month'] = data.release_date.apply(lambda x: x.split('/')[0])
data['year'] = data.release_date.apply(lambda x: x.split('/')[2])


def month_change(cell):
    """Replace the number with the name of the month"""
    if cell == '1':
        return 'January'
    if cell == '2':
        return 'February'
    if cell == '3':
        return 'March'
    if cell == '4':
        return 'April'
    if cell == '5':
        return 'May'
    if cell == '6':
        return 'June'
    if cell == '7':
        return 'July'
    if cell == '8':
        return 'August'
    if cell == '9':
        return 'September'
    if cell == '10':
        return 'October'
    if cell == '11':
        return 'November'
    if cell == '12':
        return 'December'


data['month'] = data.month.apply(month_change)
answer_27 = data.groupby(['month'])['original_title'].count().sort_values(ascending=False).index[0]

summer_season_data = data.loc[data['month'].isin(['June', 'July', 'August'])]
answer_28 = summer_season_data['original_title'].count()

winter_season_data = data.loc[data['month'].isin(['December', 'January', 'February'])]
winter_direcors_counter = Counter()
for director in winter_season_data.director.str.split('|'):
    winter_direcors_counter += Counter(director)
answer_29 = winter_direcors_counter.most_common()[0]

pivot = data.pivot_table(columns='year', index='month', values='profit', aggfunc='sum')
answer_30 = pivot.idxmax().value_counts().index[0]
