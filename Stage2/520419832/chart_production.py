'''
Chart Production
SID: 520419832

This code will design and produce some charts from the dataset previously cleaned in
"group_aggregates.py" to visually explain the trends found within the data. This code 
will closely examine the correlation between a university's success in academics and
their overall ranking as determined by various ranking platforms.

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Reading file
df_cleaned = pd.read_csv("university_rankings_cleaned.csv")

## Fixing order of categorical data
df_cleaned["age band"] = df_cleaned["age band"].astype("category")
df_cleaned["age band"] = df_cleaned["age band"].cat.set_categories(["1-9 Years", "10-24 Years", 
                                                                    "25-49 Years", "50-99 Years",
                                                                    "100+ Years"], ordered=True)

df_cleaned["size"] = df_cleaned["size"].astype("category")
df_cleaned["size"] = df_cleaned["size"].cat.set_categories(["S","M","L","XL"], ordered=True)


## Chart Creation
# Setting style
sns.set(color_codes=True)
sns.set_palette("deep")


## Chart 1 - ARWU2018 PCP vs QS2023 Overall Score, coloured by university age
'''sns.jointplot(df_cleaned, x="QS2023 Score", y="ARWU2018 Academic Performance per Capita", hue="age band",
        joint_kws={"alpha":0.75}, xlim=(0,100), ylim=(0,100), palette="CMRmap_r")'''

# Extra - AWRU2018 PCP vs QS2023 Overall Score, coloured by university size
#sns.jointplot(df_cleaned, x="QS2023 Score", y="ARWU2018 Academic Performance per Capita", hue="size",
#        joint_kws={"alpha":0.75}, xlim=(0,100), ylim=(0,100), palette="CMRmap_r")
#sns.violinplot(df_cleaned, x="size", y="QS2023 Score")
'''
The graph seems to suggest a larger universities are associated with higher QS scores, but not for ARWU.
'''


## Chart 2 - THE2020 Subject Scores by Country
country_counts = df_cleaned["location"].value_counts()
df_country = df_cleaned.groupby("location").mean().dropna().loc[country_counts >= 10]
selected = list(df_country.index.values)
sns.catplot(df_cleaned[df_cleaned["location"].isin(selected)], x="location",
            y="THE2020 Arts", kind="box")
plt.show()

