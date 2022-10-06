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
df_cleaned["size"] = df_cleaned["size"].cat.set_categories(["S", "M", "L", "XL"], ordered=True)


## Chart Creation
# Setting style
sns.set(color_codes=True)
sns.set_palette("deep")


## Chart 1 - ARWU2018 PCP vs QS2023 Overall Score, coloured by university age, sized by no. students
sns.jointplot(df_cleaned, x="QS2023 Score", y="ARWU2018 Academic Performance per Capita", hue="age band",
        joint_kws={"alpha":0.75, "size":df_cleaned["size"], "sizes":[12.5, 42.5, 105, 150]},
        xlim=(0,100), ylim=(0,100), palette="CMRmap_r")



## Chart 2 - QS2023 Reputation scores by country
# Selecting countries and cleaning dataframe
country_counts = df_cleaned["location"].value_counts()
df_country = df_cleaned.groupby("location").mean().dropna().loc[country_counts >= 10]

# Converting dataframe into wide form
df_country_long = pd.melt(df_country.reset_index(), id_vars=["location"], value_vars=["QS2023 Academic Reputation", "QS2023 Employer Reputation"])

# Graphing
sns.catplot(df_country_long, x="location", y="value", hue="variable", kind="bar")



## Chart 3 - Mean THE2020 score vs QS2023 Academic Reputation, coloured by ???
# Creating new column
df_cleaned["Mean THE2020 Score"] = (df_cleaned["THE2020 Medicine"] + df_cleaned["THE2020 Engineering"] + df_cleaned["THE2020 Law"])/3

# Graphing
sns.relplot(df_cleaned, x="Mean THE2020 Score", y="ARWU2018 Academic Performance per Capita", hue="age band", kind="scatter")
plt.show()
