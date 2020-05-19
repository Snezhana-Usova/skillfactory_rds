import pandas as pd
from collections import Counter
data = pd.read_csv('/Users/snezhanausova/skillfactory_rds/module_1/data.csv')
data['profit'] = data.revenue - data.budget
profit_data=data[data.profit > 0]
data_2012=data[data.release_year == 2012]

def profit_counter(data, column, calc_column='profit'):
    count=Counter()
    for i in range(0, len(data)):
        for x in data.iloc[i][column].split('|'):
            count[x] += data.iloc[i][calc_column]
    return(count.most_common())


answer_15 = profit_counter(data, 'director')[0]
answer_16 = profit_counter(data, 'cast')[0]
answer_17 = profit_counter(data_2012, 'cast')[-1]