import pandas as pd
import numpy as np

## Reading/Preparing Datasets
rankings = pd.read_csv("Selected/General_rankings/country_rankings.csv")

expenditure = pd.read_csv("Selected/Expenditure/Cleaned Expenditure Data.csv")
expenditure = expenditure[expenditure["Year"] == 2018].drop("Year", axis=1)
expenditure.replace({"United States of America":"United States",
                     "United Kingdom of Great Britain and Northern Ireland":"United Kingdom"}, 
                     inplace=True)

employability = pd.read_csv("Selected/Employability/Cleaned_Employability.csv")
employability.replace({"US":"United States",
                     "UK":"United Kingdom"}, 
                     inplace=True)
employability = employability.groupby("Country").min()

## Combining Datasets
combined = rankings.merge(expenditure, on="Country", how="left")
combined = combined.merge(employability, on="Country", how="left")

print(combined)

## Writing Dataset
combined.to_csv("integrated_dataset.csv", index=False)
