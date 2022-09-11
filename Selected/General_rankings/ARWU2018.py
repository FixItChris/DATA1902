import os
import pandas as pd
import numpy as np

# Reading csv file
df = pd.read_csv(os.path.abspath("ARWU/arwu.csv"), delimiter=";")

# Selecting only the relevant columns and uploading as csv (for extra analsysis in stage 2)
df = df[["University", "Country", "Year", "PCP", "Alumni", "Award", "PUB", "N&S", "Hi Ci", "World rank integer"]]
df.to_csv("ARWU/arwu_cleaned.csv", index=False)

# Selecting only the most recent data (2018) (for extra analysis in stage 2)
df_2018 = df[df["Year"] == 2018].drop("Year", axis=1)
df_2018.to_csv("ARWU/arwu2018.csv", index=False)

# Grouping the data by country to integrate with the other datasets
df_country = df_2018.groupby("Country").mean().drop("World rank integer", axis=1)
df_country.to_csv("ARWU/arwu2018_country.csv")
