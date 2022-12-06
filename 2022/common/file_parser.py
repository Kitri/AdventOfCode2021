import pandas as pd

def get_df_from_file(file_name, header, column_names):
    return pd.read_csv(file_name, header = header, names = column_names)

def read_file_old(file_name):
    f = open(file_name)

    lines = []

    with open(file_name, encoding='utf8') as f:
        lines = f.read().splitlines()

    return lines

def read_file_stripped(file_name: str) -> list:
    return [x.strip() for x in open(file_name).readlines()]

def read_file(file_name: str) -> list:
    return open(file_name).readlines()