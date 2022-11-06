# Importing / Removing unwanted columns, and producing an extracted dataset 
import pandas as pd
df = pd.read_excel("QS2023.xlsx", header=3, index_col=0)
df1 = df[['location code','size','ar score','isr score']].dropna()

#Importing the relevant bokeh elements 
from bokeh.plotting import figure, output_file, show 
from bokeh.models import BoxSelectTool, LassoSelectTool, PanTool, WheelPanTool, WheelZoomTool, ResetTool, HoverTool, Circle
tooltips = [("Average academic score", "$y")]
toolbox = [PanTool(), WheelPanTool(), WheelZoomTool(), ResetTool(), HoverTool(tooltips=tooltips )]

#Making my grouped aggregates for my barplot visualisation
uk = df1[df1['location code'] == 'UK']
us = df1[df1['location code'] == 'US']
au = df1[df1['location code'] == 'AU']
size_grouped_uk = uk.groupby('size')
size_grouped_us = us.groupby('size')
size_grouped_au = au.groupby('size')

uk_average_score = size_grouped_uk['ar score'].mean()
us_average_score = size_grouped_us['ar score'].mean()
au_average_score = size_grouped_au['ar score'].mean()

#Plot 1 of 3: UK scores grouped by size 
dict1 = uk_average_score.to_dict()

## Manually set the order of size (ig this can be step 1, as listx&y will be my x and y variables respectively)
listx = ["S", "M","L", "XL"]
listy = [dict1['S'],dict1['M'],dict1['L'],dict1['XL']] #this assigns the corresponding values (ie. the average scores) that correspond to the manually written S,M,X,Xl

#2. Telling Bokeh where to generate output 
output_file("barplot.html")

#3. using figure() to create a plot 
p = figure(x_range=listx, tools=toolbox, title='QS 2023 Rankings: Average academic reputation of UK universities by size', x_axis_label="Size", y_axis_label="Average QS 2023 Academic Reputation")
p.vbar(x=listx, top=listy, width=0.9)
##Modifying the tool cod

#5. show the plot
show(p)


