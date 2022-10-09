# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import os
from pstats import StatsProfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from collections import OrderedDict
import seaborn as sns

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

#Stage 1
xlsx = pd.ExcelFile(os.path.abspath("Selected/Employability/Times_Higher_Education_Employability.xlsx"))
df = pd.read_excel(xlsx, "Sheet1")
df_dropped = df.drop(columns=["University","Global University Employability Rank 2021"])
df_dropped.replace('(-)', np.NaN, inplace = True)
df_dropped.dropna(how="any",inplace=True)
df_dropped["Global University Employability Rank 2020"] = df_dropped["Global University Employability Rank 2020"].astype(int)
df_sorted = df_dropped.sort_values(by="Global University Employability Rank 2020",ascending=True)
df_corrrect_index = df_sorted.set_index("Global University Employability Rank 2020")
move_to = "Selected/Employability/Cleaned_Employability.csv"
df_corrrect_index.to_csv("Cleaned_Employability.csv")

#stage 2
employability_rank = pd.read_csv("Selected/Employability/Cleaned_Employability.csv")
employability_rank.replace({"US":"United States",
                     "UK":"United Kingdom"}, 
                     inplace=True)
employability_rank["Score"] = 250 - employability_rank["Global University Employability Rank 2020"]
employability_score = employability_rank.drop(columns=["Global University Employability Rank 2020"])
#print(employability_score)
num_uni_per_country = employability_score.groupby("Country").count()
num_per_country = employability_score["Country"].value_counts()
#print(num_uni_per_country)

df_country = employability_score.groupby("Country")
monke = df_country.mean().loc[num_per_country >= 9]


country_with_more_than_5_unis_in_rankings = num_uni_per_country[num_uni_per_country['Score']>8]
num_country_with_more_than_5_unis_in_rankings = num_uni_per_country[num_uni_per_country['Score']>8].count()

print(employability_score["Country"].value_counts() >= 9)
print(employability_score)
selected = ['Australia', 'Canada', 'China', 'France', 'Germany', 'Netherlands', 'United Kingdom', 'United States']
sns.catplot(employability_score[employability_score["Country"].isin(selected)], x="Country", y="Score", kind="box")
plt.show()



# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 
# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
     
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2',
                    'data_3', 'data_4'])
 
# Adding title
plt.title("Customized box plot")
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
     
# show plot
plt.show()