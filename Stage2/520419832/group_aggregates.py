'''
Group Aggregate Calculations
SID: 520419832

This code will create some grouped-aggregates from the "university_rankings.csv" csv file
(made in stage 1) to further explore the correlation between a university's age, size and
location against their relative prestige/notoriety as determined by their rankings.

'''
import pandas as pd


## Reading the file
df = pd.read_csv("university_rankings.csv")


## Cleaning the dataset
# Dropping unnecessary columns
df_dropped = df.drop(columns=["status", "ARTU Rank", "World rank integer", "ifr score_2023", "isr score_2023",
                              "ifr score_2022", "isr score_2022", "Alumni", "Award", "PUB", "N&S", "Hi Ci"])


# Renaming columns for clarity
names = {"ar score_2023":"QS2023 Academic Reputation","er score_2023":"QS2023 Employer Reputation",
        "fsr score_2023":"QS2023 Faculty Student Ratio","cpf score_2023":"QS2023 Citations per Faculty",
        "irn score":"QS2023 International Research Network","ger score":"QS2023 Employment Outcomes",
        "score scaled_2023":"QS2023 Score","ar score_2022":"QS2022 Academic Reputation",
        "er score_2022":"QS2022 Employer Reputation","fsr score_2022":"QS2022 Faculty Student Ratio",
        "cpf score_2022":"QS2022 Citations per Faculty","score scaled_2022":"QS2022 Score",
        "arts_and_humanities":"THE2020 Arts", "business_and_economics":"THE2020 Business/Economics",
        "clinical_preclinical_and_health":"THE2020 Medicine", "computer_science":"THE2020 Computer Science",
        "education":"THE2020 Education", "engineering_and_technology":"THE2020 Engineering",
        "law":"THE2020 Law", "life_sciences":"THE2020 Life Sciences",
        "phyiscal_sciences":"THE2020 Physical Sciences", "psychology":"THE2020 Psychology",
        "social_sciences":"THE2020 Social Sciences", "PCP":"ARWU2018 Academic Performance per Capita"}
df_cleaned = df_dropped.rename(columns=names)


# Changing categorical data to category type
df_cleaned["age band"] = df_cleaned["age band"].astype("category")
df_cleaned["size"] = df_cleaned["size"].astype("category")
df_cleaned["size"] = df_cleaned["size"].cat.set_categories(["S","M","L","XL"], ordered=True)


# Renaming age bins
df_cleaned["age band"].replace({1:"1-9 Years", 2:"10-24 Years", 3:"25-49 Years", 
                                4:"50-99 Years", 5:"100+ Years"}, inplace=True)


## Creating aggregates
# Overall aggregate
#print(df_cleaned.mean(numeric_only=True))


# Grouped by country - Must have at least 5 universities to be counted
'''selected = df_cleaned["location"].value_counts()
print(selected)
df_country = df_cleaned.groupby("location")
print(df_country.mean().loc[selected >= 5])'''


# Grouped by size
'''print(df_cleaned["size"].value_counts())
df_size = df_cleaned.groupby("size")
print(df_size.mean())'''


# Grouped by age
'''print(df_cleaned["age band"].value_counts())
df_age = df_cleaned.groupby("age band")
print(df_age.mean())'''
