import pandas as pd


def plot_bar(data):
    nulls = data.isnull().sum()[data.isnull().sum() > 0].plot(kind='bar')
    return nulls


def count_nulls(data):
    nulls_quantity = data.isnull().sum()[data.isnull().sum() > 0]
    return nulls_quantity
