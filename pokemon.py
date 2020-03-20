# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sbn # for data visualization

import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rcParams is a dictionary-like object for graph styles
matplotlib.rcParams['figure.subplot.wspace'] = 0.4
matplotlib.rcParams['figure.subplot.hspace'] = 0.4
matplotlib.rcParams['font.size'] = 8.0
# matplotlib.rcParams['figure.autolayout'] = True
matplotlib.rcParams['xtick.minor.size']= 1
matplotlib.rcParams['xtick.major.size']= 1
matplotlib.rcParams['xtick.minor.pad']=0
matplotlib.rcParams['xtick.major.pad']=0

# matplotlib inline

data_df = pd.read_csv("../input/PokemonGen8.csv")

data_df.drop(['Sum'], axis=1, inplace=True)
# data_df.head()
# data_df.describe()

# data_df.dtypes
data_df['type2'].fillna('NULL', inplace=True)
var_int = data_df.dtypes[data_df.dtypes=='int64'].index
var_int = var_int[1:]
var_int
l_int = len(var_int)
fig = plt.figure(figsize=(13,8))
fig.add_subplot()
for i, val in enumerate(var_int):
    fig.add_subplot(3,3,i+1)
    plt.hist(data_df[val], bins=50)
    plt.title(val)

# plt.show()
lim = 80
pokeH_df = data_df[(data_df['hp']>=lim)&((data_df['attack']>=lim)&(data_df['sp_attack']>=data_df['attack']))&
                          ((data_df['defense']>=lim)|(data_df['sp_defense']>=data_df['defense']))]

fig = plt.figure(figsize=(13,24))
for i,col in enumerate(var_int[:6]):
    ax1 = fig.add_subplot(6,1,i+1)
    sbn.boxplot(x=pokeH_df['type1'], y=pokeH_df[col], ax=ax1)       

plt.show()
