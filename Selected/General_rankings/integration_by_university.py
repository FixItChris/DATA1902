import pandas as pd
import numpy as np


## Creating by university (extra analysis)
# Reading Datasets:
qs2023 = pd.read_csv("QS/QS2023_cleaned.csv").drop(["size", "focus", "research", "age band", "status"],axis=1)
qs2022 = pd.read_csv("QS/QS2022_cleaned.csv").drop(["size", "focus", "research", "age band", "status"],axis=1)
artu2021 = pd.read_csv("ARTU/ARTU_Ranks.csv")
the2020 = pd.read_csv("THE/THE2020_bysubject_uni.csv")
arwu2018 = pd.read_csv("ARWU/arwu2018.csv")

# Merging Datasets:
combined = qs2023.merge(qs2022, on="institution", suffixes=["_2023","_2022"]).drop("country", axis=1)
combined = combined.merge(artu2021, how="left", left_on="institution", right_on="University Name", 
            suffixes=["", "_2021"]).drop(["University Name", "Country"], axis=1)
combined = combined.merge(the2020, how="left", left_on="institution", right_on="university_name",
            suffixes=["", "_2020"]).drop("university_name", axis=1)
combined = combined.merge(arwu2018, how="left", left_on="institution", right_on="University",
            suffixes=["", "_2018"]).drop(["University","Country"], axis=1)

# Writing Dataset:
combined.to_csv("university_rankings.csv", index=False)
