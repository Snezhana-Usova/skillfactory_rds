import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]
data_2012 = data[data.release_year == 2012]
data_2015 = data[data.release_year == 2015]
comedy_data = data[data['genres'].str.contains('Comedy')]


def movies_count(data, column='production_companies'):
    """Return number of movies per each production company"""
    count = Counter()
    for i in range(0, len(data)):
        for x in data.iloc[i][column].split('|'):
            count[x] += 1
    return count.most_common()


answer_20 = movies_count(data)[0]
answer_21 = movies_count(data_2015)[0]


def profit_counter(data, column='production_companies', calc_column='profit'):
    """Return total profit per each production company"""
    count = Counter()
    for i in range(0, len(data)):
        for x in data.iloc[i][column].split('|'):
            count[x] += data.iloc[i][calc_column]
    return count.most_common()


answer_22 = profit_counter(comedy_data)[0]
answer_23 = profit_counter(data_2012)[0]
