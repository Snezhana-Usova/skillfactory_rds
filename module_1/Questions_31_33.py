import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')

title_count = pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts().reset_index()
title_count.columns = ['Company', 'Titles_count']


def symbols_count(data, column='production_companies', calc_column='original_title'):
    """Return number of symbols in movie titles per each production company"""
    count = Counter()
    for i in range(0, len(data)):
        for company in data.iloc[i][column].split('|'):
            count[company] += len(data.iloc[i][calc_column])
    return count.most_common()


symbol_count = pd.DataFrame(symbols_count(data))
symbol_count.columns = ['Company', 'Symbols_count']
joined = title_count.merge(symbol_count, on='Company', how='left')
joined['Mean'] = joined['Symbols_count']/joined['Titles_count']
answer_31 = joined[joined.Mean == joined.Mean.max()]['Company']


def words_count(data, column='production_companies', calc_column='original_title'):
    """Return number of words in movie titles per each production company"""
    count = Counter()
    for i in range(0, len(data)):
        for company in data.iloc[i][column].split('|'):
            count[company] += len(data.iloc[i][calc_column].split(' '))
    return count.most_common()


word_count = pd.DataFrame(words_count(data))
word_count.columns = ['Company', 'Words_count']
joined = title_count.merge(word_count, on='Company', how='left')
joined['Mean'] = joined['Words_count']/joined['Titles_count']
answer_32 = joined[joined.Mean == joined.Mean.max()]

data['original_title'] = data.original_title.apply(lambda w: str(w).lower())
answer_33 = pd.DataFrame(data.original_title.str.split(' ').tolist()).stack().replace('-', '').nunique()
