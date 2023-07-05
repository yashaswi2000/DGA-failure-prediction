import pandas as pd

def twoGasRatioUtil(dataframe: object, col1: str, col2: str) -> object:
    dataframe[col1 + '/' + col2] = dataframe[col1]/dataframe[col2]
    dataframe[col2 + '/' + col1] = dataframe[col2]/dataframe[col1]
    print(dataframe)
    return dataframe


    