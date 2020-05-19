import pandas as pd
import numpy as np

from collections import Counter
from itertools import combinations

data = pd.read_csv('data.csv')
data['profit'] = data.revenue - data.budget
profit_data = data[data.profit > 0]

answer_34 = data.sort_values('vote_average', ascending=False)[0:round(len(data) / 100)]['original_title']
answer_35 = Counter(np.sum([list(combinations(x, 2)) for x in data.cast.str.split('|')])).most_common(1)

director_count = pd.DataFrame(data.director.str.split('|').tolist()).stack().value_counts().reset_index()
director_count.columns = ['Director', 'Movie_count']
director_profit_count = pd.DataFrame(profit_data.director.str.split('|').tolist()).stack().value_counts().reset_index()
director_profit_count.columns = ['Director', 'Movie_profit_count']
joined = director_profit_count.merge(director_count, on='Director', how='inner')
joined['Mean'] = (joined['Movie_profit_count'] / joined['Movie_count']) * 100
joined.sort_values('Mean', ascending=False)
answer_36 = joined.loc[joined['Director'].isin(['Steven Soderbergh', 'Robert Rodriguez', 'Quentin Tarantino',
                                                'Christopher Nolan', 'Clint Eastwood'])
                       ].sort_values('Mean', ascending=False)
