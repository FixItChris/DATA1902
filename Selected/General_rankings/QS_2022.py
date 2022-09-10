import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Importing / Removing unwanted columns
df = pd.read_excel(os.path.abspath("QS/QS2022.xlsx"), header=3, index_col=2)
df_dropped = df.drop(columns=['rank in country', 'rank in subregion', 'rank display2', 'country code', 'ar rank', 'er rank', 'fsr rank', 'cpf rank', 'ifr rank', 'isr rank'])

## Cleaning - Datatypes - issue with '-' in overall score; size bins now interpreted correctly
df_dropped['age band'] = df_dropped['age band'].astype(object)
df_dropped.replace('-', np.NaN, inplace = True) # Impute with value? (<25)
df_dropped['score scaled'] = df_dropped['score scaled'].astype(float)
df_dropped.to_csv("QS/QS2022_cleaned.csv", index=False)
#print(df_dropped.info())

## General summary
#print(df.columns)
#print(df.head())
#print(df.info())
#print(df.describe())


## Grouping by country - Comparing overall scores
df_grouped = df_dropped.dropna().groupby("country")[['ar score', 'er score', 'fsr score', 'cpf score', 'ifr score', 'isr score', 'score scaled']]
df_country_mean = df_grouped.mean()
df_country_mean.to_csv("QS/QS2022_bycountry.csv")


## Analysis of overall score (update)
#print(df_grouped.mean())
#print(df_grouped.describe().sort_values('count', ascending=False)) # No. universities in top 500
#print(df_grouped.describe().sort_values('mean', ascending=False)) # Sorted by mean
#print(df_grouped.describe().sort_values('50%', ascending=False)) # Sorted by median

## Simple histogram of overall scores
#sns.histplot(data=df_dropped.dropna(), x='score scaled')
#plt.show()
