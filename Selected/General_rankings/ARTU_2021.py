import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_html("http://research.unsw.edu.au/artu/artu-results")[0]
df.drop("Unnamed: 0", axis=1, inplace=True)
#print(df.info())

artu_ranks = df[["University Name", "Country",  "ARTU Rank"]]
#print(artu_ranks.shape)
artu_ranks.to_csv("ARTU/ARTU_Ranks.csv", index=False)

df_grouped = df.groupby("Country")["ARTU Rank"].mean()
#print(df_grouped.info())
df_grouped.to_csv("ARTU/ARTU_Country.csv")
