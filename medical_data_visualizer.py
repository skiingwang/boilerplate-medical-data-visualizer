import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight']/(df['height']/100)**2 > 25).astype(np.int8)

# 3
df['cholesterol'] = df['cholesterol'].gt(1).astype(np.int8)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='value')


    # 6
    df_cat1 = df.groupby(['cardio']).count()
    

    # 7
    long_df = pd.melt(df_cat1, id_vars=['id'], value_vars=['age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='value')


    # 8
    fig = sns.scatterplot(data=df_cat, x='value')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
