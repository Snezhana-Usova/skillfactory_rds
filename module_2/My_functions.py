import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind


def change_to_object(column, data):
    """Cast pandas serias to object dtype"""
    data[column] = data[column].astype('object')


def print_summary(column, data):
    """Print summary of column"""
    print(data[column].describe())
    print()
    print('Количество уникальных значений:', data[column].nunique())
    print('Количество пустых значений:', data[column].isnull().sum())


def get_countplot(column, data):
    """Build a countplot"""
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.countplot(x=column, data=data, ax=ax)
    ax.set_title('Countplot for ' + column)
    plt.show()


def get_boxplot(column, target_column, data):
    """Build a boxplot"""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x=column, y=target_column, data=data, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()


def get_barplot(column, target_column, data):
    """Build a barplot"""
    fig, ax = plt.subplots(figsize=(9, 3))
    sns.barplot(x=column, y=target_column, data=data, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Barplot for ' + column)
    plt.show()


def fill_data(column, data):
    """Fill NAN values with the most frequent value"""
    data[column].fillna(data[column].value_counts().index[0], inplace=True)


def get_stat_dif(column, target_column, data, alpha):
    """Use the T-test to find columns with statistically significant differences"""
    cols = data.loc[:, column].value_counts().index[:]
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        a = data.loc[data.loc[:, column] == comb[0], target_column]
        b = data.loc[data.loc[:, column] == comb[1], target_column]
        result = ttest_ind(a, b).pvalue

        if result <= alpha/len(combinations_all):
            print('Найдены статистически значимые различия для колонки', column)
            break
