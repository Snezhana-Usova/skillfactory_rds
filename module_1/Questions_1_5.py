import pandas as pd
data = pd.read_csv('data.csv')

answer_1 = data[data.budget == data.budget.max()]['original_title']
answer_2 = data[data.runtime == data.runtime.max()]['original_title']
answer_3 = data[data.runtime == data.runtime.min()]['original_title']
answer_4 = round(data.runtime.mean())
answer_5 = round(data.runtime.median())
