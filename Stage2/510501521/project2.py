import matplotlib.pyplot as plt
import pandas as pd

## Importing / Removing unwanted columns, and producing an extracted dataset 
df = pd.read_excel("/Users/johnnyc/Desktop/Project 2/QS2023.xlsx", header=3, index_col=0)
df1 = df[['location code','size','ar score','isr score']]

#Grouped aggregate 1: How great is the impact of the university size in terms of the academic performance of a university?
uk = df1[df['location code'] == 'UK']
us = df1[df['location code'] == 'US']
au = df1[df['location code'] == 'AU']
size_grouped_uk = uk.groupby('size')
size_grouped_us = us.groupby('size')
size_grouped_au = au.groupby('size')
# Analysing the average academic reputation for each country's universities grouped by their respective size 
uk_average_score = size_grouped_uk['ar score'].mean()
us_average_score = size_grouped_us['ar score'].mean()
au_average_score = size_grouped_au['ar score'].mean()
print(uk_average_score, us_average_score,au_average_score)


#Grouped  aggregate 2: How does the composition of international students differ between Australia and US?
bin1 = [0,25,50,75,100]
bin_name = ['0-25','25-50','50-75','75-100']
#Extracting out the relevant countries
us1 = df[df['location code'] == 'US']
au1 = df[df['location code'] == 'AU']

#Producing the desired output for each country - grouped aggragate values
n, bins, patches = plt.hist(au1["isr score"], bins=bin1, edgecolor='black')
for i in range(len(n)):
    plt.text(bins[i], n[i]*1.02, int(n[i]), fontsize=12, horizontalalignment="center")

n, bins, patches = plt.hist(us1["isr score"], bins=bin1, edgecolor='black')
for i in range(len(n)):
    plt.text(bins[i], n[i]*1.02, int(n[i]), fontsize=12, horizontalalignment="center")

#Producing the desired output for each country - grouped aggragate charts
plt.hist(au1['isr score'], bins=bin1, edgecolor='black')
plt.title('International students composition in Australia')
plt.xlabel('International students score')
plt.ylabel('Total number of universities')
plt.show()

plt.hist(us1['isr score'], bins=bin1, edgecolor='black')
plt.title('International students composition in the United States')
plt.xlabel('International students score')
plt.ylabel('Total number of universities')
plt.show()



