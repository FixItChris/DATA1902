import pandas as pd

'''combined = pd.read_csv("university_rankings.csv")
the = pd.read_csv("the.txt")
the = the[the["year"] == 2020]

#print(the)
#print(combined)
df = pd.merge(combined, the, how="left", left_on="institution", right_on="university_name")
df.to_csv("QS_THE.csv", index=False)
print(df)'''

df = pd.read_csv("THE_QS.csv")
df["total_score"] = df["teaching"]*0.3 + df["research"]*0.3 + df["citations"]*0.3 + df["international"]*0.075 + df["income"]*0.025
print(df.dropna())
df.to_csv("THE_QS_cleaned.csv", index=False)