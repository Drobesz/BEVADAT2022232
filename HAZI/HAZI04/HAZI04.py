import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def csv_to_df(file): return pd.read_csv(file)
def capitalize_columns(df):
    new_df = df.copy()
    new_df.columns = [item if 'e' in item else item.upper() for item in new_df.columns]
    return new_df
def math_passed_count(df):
    new_df = df.copy()
    return (new_df['math score'] >= 50).sum()
def did_pre_course(df):
    new_df = df.copy()
    return new_df[new_df['test preparation course'] == 'completed']
def average_scores(df):
    new_df = df.copy()
    return new_df.groupby(['parental level of education']).mean()
def add_grade(df):
    new_df = df.copy()
    new_df['grade'] =   np.where((new_df['math score'] + new_df['reading score'] + new_df['writing score']) < 180, 'F',
                        np.where((new_df['math score'] + new_df['reading score'] + new_df['writing score']) < 210, 'D', 
                        np.where((new_df['math score'] + new_df['reading score'] + new_df['writing score']) < 240, 'C',
                        np.where((new_df['math score'] + new_df['reading score'] + new_df['writing score']) < 270, 'B', 'A'))))
    return new_df

'''
testdata = csv_to_df('HAZI\HAZI04\StudentsPerformance.csv')
print(capitalize_columns(testdata))
print(math_passed_count(testdata))
print(did_pre_course(testdata))
print(average_scores(testdata))
print(add_grade(testdata))
'''