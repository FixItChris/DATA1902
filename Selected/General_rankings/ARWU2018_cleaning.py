import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(os.path.abspath("ARWU/arwu.csv"), delimiter=";")
df = df[["University", "Country", "Year", "PCP", "Alumni", "Award", "PUB", "N&S", "Hi Ci", "World rank integer"]]
print(df)
#df.to_csv("ARWU/arwu_cleaned.csv", index=False)

df_2018 = df[df["Year"] == 2018].drop("Year", axis=1)
print(df_2018)
#df_2018.to_csv("ARWU/arwu2018.csv", index=False)

df_country = df_2018.groupby("Country").mean().drop("World rank integer", axis=1)
print(df_country)
df_country.to_csv("ARWU/arwu2018_country.csv")

