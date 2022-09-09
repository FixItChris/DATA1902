import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(os.path.abspath("THE/THE_by_subject.csv"), index_col=0)
df2020 = df[df['year']==2020] # View only newest data

#print(df2020)

## Pivoting table to merge with other datasets (by country)
country_subject = df2020.groupby(["country","subject"]).median().reset_index()
#print(country_subject)
coutry_subject_pivot = country_subject.pivot(index="country", columns="subject", values="total_score")
#print(country_subject_pivot)


## By uni (for extra analysis)
uni_subject = df2020.groupby(["university_name","subject"]).median().reset_index()
#print(uni_subject)
uni_subject_pivot = uni_subject.pivot(index="university_name", columns="subject", values="total_score")
print(uni_subject_pivot)
