#The purpose of this code is to remove the row's with invalid rows, and we remove universityies and remove 2020 data and afterwards averaging the data by country.
import numpy as np
import pandas as pd


xlsx = pd.ExcelFile("DATA1902\Selected\Employability\Times_Higher_Education_Employability.xlsx")
df = pd.read_excel(xlsx, "Sheet1")

#Used to remove in specified columns
df_dropped = df.drop(columns=["University","Global University Employability Rank 2021"])

#used to remove rows with null values
df_dropped.replace('(-)', np.NaN, inplace = True)

df_dropped.dropna(how="any",inplace=True)

#df_dropped.sort_values(axis=1, by="Global University Employability Rank 2020",ascending=False)
df_sorted = df_dropped.sort_values(by="Global University Employability Rank 2020",ascending=True)
df_corrrect_index = df_sorted.set_index("Global University Employability Rank 2020")
print(df_sorted)
move_to = "DATA1902\Selected\Employability\Cleaned_Employability.csv"
df_corrrect_index.to_csv(move_to)






