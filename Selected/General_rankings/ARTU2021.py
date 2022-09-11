import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading File / Dropping unneeded columns
df = pd.read_html("http://research.unsw.edu.au/artu/artu-results")[0]
df.drop("Unnamed: 0", axis=1, inplace=True)
artu_ranks = df[["University Name", "Country",  "ARTU Rank"]]

# Writing to csv
artu_ranks.to_csv("ARTU/ARTU_Ranks.csv", index=False)

# Writing data grouped by country to csv
df_grouped = df.groupby("Country")["ARTU Rank"].mean()
df_grouped.to_csv("ARTU/ARTU_Country.csv")
