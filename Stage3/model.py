import numpy as np
import pandas as pd


df = pd.read_csv("university_rankings_cleaned.csv")


print(df["ARWU2018 Academic Performance per Capita"].dropna())

