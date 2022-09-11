import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Trying to read website file - only read first 30 rows
#df = pd.read_html("https://www.shanghairanking.com/rankings/arwu/2022")[0]
#df.drop(["Unnamed: 2", "National/Regional Rank", "Unnamed: 5"], axis=1, inplace=True)


df = pd.read_csv(os.path.abspath("ARWU/arwu.csv"), delimiter=";")
df = df[["University", "Country", "Year", "PCP", "Alumni", "Award", "PUB", "N&S", "Hi Ci", "World rank integer"]]
print(df)
df.to_csv("ARWU/arwu_cleaned.csv", index=False)

df_2018 = df[df["Year"] == 2018].drop("Year", axis=1)
print(df_2018)
df_2018.to_csv("ARWU/arwu2018.csv", index=False)

