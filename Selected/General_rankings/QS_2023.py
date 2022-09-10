import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Importing / Removing unwanted columns
#df = pd.read_csv("QS/QS World University Rankings 2022.csv")
df = pd.read_excel("QS/QS2023.xlsx", header=3, index_col=0)
df_dropped = df.drop(columns=['rank display2', 'location code', 'ar rank', 'er rank', 'fsr rank', 'cpf rank', 'ifr rank', 'isr rank', 'irn rank', 'ger rank'])

## Cleaning - Datatypes - issue with '-' in overall score; size bins now interpreted correctly
df_dropped['age band'] = df_dropped['age band'].astype(object)
df_dropped.replace('-', np.NaN, inplace = True)
df_dropped['score scaled'] = df_dropped['score scaled'].astype(float)
df_dropped.to_csv("QS/QS2023_cleaned.csv", index=False)
print(df_dropped.info())

## General summary
'''print(df.columns)
print(df.head())
print(df.info())
print(df.describe())'''

## Grouping by country - Comparing overall scores
df_grouped = df_dropped.dropna().groupby("location")[['ar score', 'er score', 'fsr score', 'cpf score', 'ifr score', 'isr score', 'irn score', 'ger score', 'score scaled']]
df_country_mean = df_grouped.mean()
df_country_mean.to_csv("QS/QS2023_bycountry.csv")

#print(df_grouped.describe().sort_values('count', ascending=False)) # No. universities in top 500
#print(df_grouped.describe().sort_values('mean', ascending=False)) # Sorted by mean
#print(df_grouped.describe().sort_values('50%', ascending=False)) # Sorted by median

## Simple histogram of overall scores
#sns.histplot(data=df_dropped.dropna(), x='score scaled')
#plt.show()


