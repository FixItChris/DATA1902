import pandas as pd
import numpy as np

## Reading Datasets
rankings = pd.read_csv("Selected/General_rankings/country_rankings.csv")
expenditure = pd.read_csv("Selected/Expenditure/Cleaned Expenditure Data.csv")
expenditure = expenditure[expenditure["Year"] == 2018].drop("Year", axis=1)

## Combining Datasets
combined = rankings.merge(expenditure, on="Country", how="left")

## Writing Dataset
combined.to_csv("integrated_dataset.csv", index=False)
