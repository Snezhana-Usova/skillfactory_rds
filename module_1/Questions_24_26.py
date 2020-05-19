import pandas as pd

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]

Param_Pict_data = data[data['production_companies'].str.contains('Paramount Pictures')]
Warner_Bros_data = data[data['production_companies'].str.contains('Warner Bros')]

answer_24 = Param_Pict_data[Param_Pict_data.profit == Param_Pict_data.profit.min()]['original_title']
answer_25 = data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False).index[0]
answer_26 = Warner_Bros_data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False).index[0]
