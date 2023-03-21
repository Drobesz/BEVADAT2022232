import pandas as pd
import matplotlib.pyplot as plt

def dict_to_dataframe(dict): return pd.DataFrame(dict)
def get_column(df, area): 
    df_new = df.copy()
    return df_new['area']
def get_top_two(df):
    df_new = df.copy()
    return df_new.sort_values(by='area', ascending=False)[0:2]
def population_density(df):
    df_new = df.copy()
    df_new['density'] = df_new['population'] / df_new['area']
    return df_new
def plot_population(df):
    df_new = df.copy()
    fig, ax = plt.subplots()
    ax.bar(df_new['country'], df_new['population'])
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')
    ax.set_title('Population of Countries')
    #fig.suptitle('Population of Countries')
    return fig
def plot_area(df):
    df_new = df.copy()
    fig, ax = plt.subplots()
    ax.pie(df_new['area'], autopct='%1.1f%%', startangle=90)
    ax.set_title('Area of Countries')
    return fig

stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

testdata = dict_to_dataframe(stats)

'''
print(get_column(testdata, "area"))
print(get_top_two(testdata))
print(population_density(testdata))
valami = plot_area(testdata)
plt.show()
'''