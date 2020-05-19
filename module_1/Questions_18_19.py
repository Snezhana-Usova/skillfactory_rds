import pandas as pd

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]
high_budget = data[data.budget > data.budget.mean()]
nicolas_cage = data[data['cast'].str.contains('Nicolas Cage')]

answer_18 = pd.DataFrame(high_budget.cast.str.split('|').tolist()).stack().value_counts().index[0]
answer_19 = pd.DataFrame(nicolas_cage.genres.str.split('|').tolist()).stack().value_counts().index[0]
