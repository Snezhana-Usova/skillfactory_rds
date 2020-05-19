import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]

genre_counter = Counter()
for genre in data.genres.str.split('|'):
    genre_counter += Counter(genre)
answer_11 = genre_counter.most_common()[0]

profit_genre_counter = Counter()
for genre in profit_data.genres.str.split('|'):
    profit_genre_counter += Counter(genre)
answer_12 = profit_genre_counter.most_common()[0]
answer_13 = pd.DataFrame(data.director.str.split('|').tolist()).stack().value_counts().head().index[0]
answer_14 = pd.DataFrame(profit_data.director.str.split('|').tolist()).stack().value_counts().head().index[0]
