import os
import numpy as np
import pandas as pd

## Reading file
df = pd.read_csv(os.path.abspath("THE/THE_original.csv"), index_col=0)

## Selecting only the newest data (2020)
df2020 = df[df['year']==2020] 

## Pivoting table to merge with other datasets (by country)
country_subject = df2020.groupby(["country","subject"]).median().reset_index()
country_subject_pivot = country_subject.pivot(index="country", columns="subject", values="total_score")
country_subject_pivot.to_csv("THE/THE2020_bysubject_country.csv")

## By university (for extra analysis in stage 2)
uni_subject = df2020.groupby(["university_name","subject"]).median().reset_index()
uni_subject_pivot = uni_subject.pivot(index="university_name", columns="subject", values="total_score")
uni_subject_pivot.to_csv("THE/THE2020_bysubject_uni.csv")
