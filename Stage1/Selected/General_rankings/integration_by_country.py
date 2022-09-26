import pandas as pd
import numpy as np

## Reading Datasets
QS2023 = pd.read_csv("QS/QS2023_bycountry.csv").rename(columns={"location":"Country"})
QS2022 = pd.read_csv("QS/QS2022_bycountry.csv").rename(columns={"country":"Country"})
ARTU2021 = pd.read_csv("ARTU/ARTU_Country.csv")
THE2020 = pd.read_csv("THE/THE2020_bysubject_country.csv").rename(columns={"country":"Country"})
ARWU2018 = pd.read_csv("ARWU/arwu2018_country.csv").rename(columns={"country":"Country"})


## Combining Datasets
combined = QS2023.merge(QS2022, how="left", on="Country", suffixes=["_QS2023", "_QS2022"])
combined = combined.merge(ARTU2021, how="left", on="Country", suffixes=["", "_ARTU2021"])
combined = combined.merge(THE2020, how="left", on="Country", suffixes=["", "_THE2020"])
combined = combined.merge(ARWU2018, how="left", on="Country", suffixes=["", "_ARWU2018"])


## Writing Dataset
combined.to_csv("country_rankings.csv", index=False)
