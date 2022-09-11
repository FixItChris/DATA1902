import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Importing / Removing unwanted columns
df = pd.read_excel("QS/QS2023.xlsx", header=3, index_col=0)
df_dropped = df.drop(columns=['rank display2', 'location code', 'ar rank', 'er rank', 'fsr rank',
                              'cpf rank', 'ifr rank', 'isr rank', 'irn rank', 'ger rank'])


## Cleaning - issue with '-' in overall score; size bins now interpreted correctly
df_dropped['age band'] = df_dropped['age band'].astype(object)
df_dropped.replace('-', np.NaN, inplace = True)
df_dropped['score scaled'] = df_dropped['score scaled'].astype(float)
df_dropped.to_csv("QS/QS2023_cleaned.csv", index=False)


## Grouping by country - Comparing overall scores
df_grouped = df_dropped.dropna().groupby("location")[['ar score', 'er score', 'fsr score',
            'cpf score', 'ifr score', 'isr score', 'irn score', 'ger score', 'score scaled']]
df_country_mean = df_grouped.mean()


## Writing to csv file
df_country_mean.to_csv("QS/QS2023_bycountry.csv")



## Analysis
# Simple histogram of overall scores for each university
sns.histplot(data=df_dropped.dropna(), x='score scaled')
plt.show()

# Viewing the 10 highest ranking universities:
print(df_dropped.head(10))

# Viewing the 5 highest average final scores of each country:
print(df_dropped.groupby("location")["score scaled"].describe().sort_values("mean", ascending=False).head())
