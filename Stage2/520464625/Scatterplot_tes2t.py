#The purpose of this code is to remove the row's with invalid rows, and we remove universityies and remove 2020 data.
import os
from pstats import StatsProfile
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from collections import OrderedDict
import seaborn as sns
import matplotlib.cm as cm

#read data
xlsx = pd.ExcelFile(os.path.abspath("DATA1902\Selected\Employability\Times_Higher_Education_Employability.xlsx"))
df = pd.read_excel(xlsx, "Sheet1")

#Used to remove in specified columns
df_dropped = df.drop(columns=["University","Global University Employability Rank 2021"])

#used to remove rows with null values
df_dropped.replace('(-)', np.NaN, inplace = True)

df_dropped.dropna(how="any",inplace=True)
df_dropped["Global University Employability Rank 2020"] = df_dropped["Global University Employability Rank 2020"].astype(int)

#sort uni's country by 2020 rankings.
df_sorted = df_dropped.sort_values(by="Global University Employability Rank 2020",ascending=True)
df_corrrect_index = df_sorted.set_index("Global University Employability Rank 2020")

#Lists uni's per country
#df_grouped = df_corrrect_index.groupby(by="Country").value_counts()

#List of country's
#df_grouped = df_corrrect_index.groupby(by="Country").count()

#print(df_grouped)   

#move data to new file
move_to = "DATA1902\Selected\Employability\Cleaned_Employability.csv"
df_corrrect_index.to_csv("Cleaned_Employability.csv")


employability_rank = pd.read_csv("DATA1902\Selected\Employability\Cleaned_Employability.csv")
employability_rank.replace({"US":"United States",
                     "UK":"United Kingdom"}, 
                     inplace=True)
employability_rank["Score"] = 250 - employability_rank["Global University Employability Rank 2020"]
employability_score = employability_rank.drop(columns=["Global University Employability Rank 2020"])
#print(employability_score)

num_uni_per_country = employability_score["Country"].value_counts()
#print(num_uni_per_country)

df_country = employability_score.groupby("Country")
monke = df_country.mean().loc[num_uni_per_country >= 9]
mean_score_country = monke.reset_index()
move_to = "DATA1902\Selected\Employability\Average_score.xlsx"
monke.to_excel(move_to)

#print(mean_score_country.to_string())

df1 = employability_score
df2 = mean_score_country

for i in range(len(df1["Country"])):
    
    
    if df1["Country"][i] in df2["Country"].to_list():

        index =  df2["Country"].to_list().index(df1["Country"][i])

        if "Average_score" not in df1.columns:
            
            df1["Average_score"] = df2["Score"][index]
            
        else:
            df1["Average_score"][i] = df2["Score"][index]
    else:
        df1["Average_score"][i] = np.NaN
#print(df1.to_string())
df1 = df1.dropna()
df1= df1.reset_index()


sns.scatterplot(x=df1["Score"],y=df1["Average_score"], hue=df1["Country"],legend='full', palette ='Dark2')

plt.show()


