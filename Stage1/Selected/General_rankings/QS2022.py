import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Importing / Removing unwanted columns
df = pd.read_excel(os.path.abspath("QS/QS2022_original.xlsx"), header=3, index_col=2)
df_dropped = df.drop(columns=['rank in country', 'rank in subregion', 'rank display2',
        'country code', 'ar rank', 'er rank', 'fsr rank', 'cpf rank', 'ifr rank', 'isr rank'])

## Cleaning - issue with '-' in overall score; size bins now interpreted correctly
df_dropped['age band'] = df_dropped['age band'].astype(object)
df_dropped.replace('-', np.NaN, inplace = True)
df_dropped['score scaled'] = df_dropped['score scaled'].astype(float)
df_dropped.to_csv("QS/QS2022_cleaned.csv", index=False)

## Grouping by country - Comparing overall scores
df_grouped = df_dropped.dropna().groupby("country")[['ar score', 'er score', 'fsr score',
        'cpf score', 'ifr score', 'isr score', 'score scaled']]
df_country_mean = df_grouped.mean()
df_country_mean.to_csv("QS/QS2022_bycountry.csv")


## Analysis
# Simple histogram of overall scores
sns.histplot(data=df_dropped.dropna(), x='score scaled')
plt.show()

# Viewing the 10 highest ranking universities:
print(df_dropped.head(10))

# Viewing the 5 highest average final scores of each country:
print(df_dropped.groupby("country")["score scaled"].describe().sort_values("mean", ascending=False).head())
