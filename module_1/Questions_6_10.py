import pandas as pd

data = pd.read_csv('data.csv')
data["profit"] = data.revenue - data.budget
year_2008 = data[data.release_year == 2008]
year_2012_2014 = data[(data.release_year >= 2012) & (data.release_year <= 2014)]

answer_6 = data[data.profit == data.profit.max()]['original_title']
answer_7 = data[data.profit == data.profit.min()]['original_title']
answer_8 = data[data.revenue > data.budget].imdb_id.nunique()
answer_9 = year_2008[year_2008.profit == year_2008.profit.max()]['original_title']
answer_10 = year_2012_2014[year_2012_2014.profit == year_2012_2014.profit.min()]['original_title']
