import pandas as pd
import numpy as np

df = pd.read_excel("CWTS Leiden Ranking 2022.xlsx", sheet_name=1)
df_cleaned = df[df["Period"] == "2017-2020"]
df_cleaned = df[df["Frac_counting"] == 0]
df_cleaned = df_cleaned.drop(["Period", "Frac_counting"], axis=1)

df_grouped = df_cleaned.groupby("Country").mean()

df_grouped.to_csv("CWTS2020.csv")
