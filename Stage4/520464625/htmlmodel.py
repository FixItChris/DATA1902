import numpy as np
import math
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import BoxSelectTool, PanTool, WheelZoomTool, ResetTool, HoverTool,SaveTool,LassoSelectTool,Circle,ColumnDataSource
from bokeh.layouts import gridplot


#output file  
output_file("pog.html")


#Gathering my data
rankings = pd.read_csv("Stage3/520464625/integrated_dataset.csv")
#Important to make the lists/series/array the same size
rankings_restricted = rankings.dropna()
#I was unsure which data to takeout, and this system makes sure I can easily change the column extracted.
extra1 = "QS2023 Employer Reputation"
extra2 = "QS2023 Faculty Student Ratio"
extra3 = "QS2023 Citations per Faculty"
#First data variables
#linking the data together, for selection tools.
ColumnDataSource
data = {extra1: rankings_restricted[extra1],
        extra2: rankings_restricted[extra2],
        extra3: rankings_restricted[extra3],
        "QS2023 Academic Reputation": rankings_restricted["QS2023 Academic Reputation"],
        "THE2020 Overall Score":rankings_restricted["THE2020 Overall Score"]
        }
source = ColumnDataSource(data=data)
#My list of interactive tools
tools = [
        #I set the box select tool to width because there is always a direct correlation between y values if the y values are the same
        #As a result I restricted the the tool to only the width, so that the user can only look at the correlation between the x variables.
        BoxSelectTool(dimensions="width"), 
        #The pan + wheel zoom tools, allow for the user to move around while zoomed in, if they wihs to only look at specific parts.
        PanTool(),  
        WheelZoomTool(),
        #
        ResetTool(),
        #Allows the user to see the point, and their corresponding values
        # Unfortunately bokeh, unlike the boxselect tool, can not hover a point, and show it's repective other points
        HoverTool(),
        #Allows the user to save the modified version of the data.
        SaveTool()
         ]
#Initilizing the graph
p1 = figure(title="QS2023 Academic Reputation and THE2020 Overall Score",
           tools=tools,
           #all the scores are beteween 0 and 100
           x_range=(0, 100),
           y_range=(0, 100),
           x_axis_label="QS2023 Academic Reputation",
           y_axis_label="THE2020 Overall Score")
#This is a customization towards the select, box and lasso tools, There is a reason for the different colours, explained in the report.
r = p1.circle(x = "QS2023 Academic Reputation", 
             y = "THE2020 Overall Score"
             , source =  source,fill_color="lightgreen", size=10, alpha=0.5,line_color=None)
r.selection_glyph = Circle(fill_color="lightgreen", line_color=None, fill_alpha=1)
r.nonselection_glyph = Circle(fill_color=None, line_color=None, fill_alpha=0.25)

#show(p1)#Making sure graph 1 works 

#graph 2
p2 =  figure(title = extra1 + " and THE2020 Overall Score",
            tools=tools,
            #all the scores are beteween 0 and 100
            x_range=(0, 100),
            y_range=(0, 100),
            x_axis_label= extra1  ,
            y_axis_label="THE2020 Overall Score"
            )

r = p2.circle(x = extra1, y = "THE2020 Overall Score", source =  source,fill_color="orange", size=10, alpha=0.5,line_color=None)
r.selection_glyph = Circle(fill_color="orange", line_color=None, fill_alpha=1)
r.nonselection_glyph = Circle(fill_color=None, line_color=None, fill_alpha=0.25)

#graph 3
p3 =  figure(title = extra2 + " and THE2020 Overall Score",
            tools=tools,
            #all the scores are beteween 0 and 100
            x_range=(0, 100),
            y_range=(0, 100),
            x_axis_label= extra2  ,
            y_axis_label="THE2020 Overall Score"
            )

r = p3.circle(x = extra2, y = "THE2020 Overall Score", source =  source,fill_color="violet", size=10, alpha=0.5,line_color=None)
r.selection_glyph = Circle(fill_color="violet", line_color=None, fill_alpha=1)
r.nonselection_glyph = Circle(fill_color=None, line_color=None, fill_alpha=0.25)

#graph 4
p4 =  figure(title = extra3 + " and THE2020 Overall Score",
            tools=tools,
            #all the scores are beteween 0 and 100
            x_range=(0, 100),
            y_range=(0, 100),
            x_axis_label= extra3  ,
            y_axis_label="THE2020 Overall Score"
            )

r = p4.circle(x = extra3, y = "THE2020 Overall Score", source =  source,fill_color="turquoise", size=10, alpha=0.5,line_color=None)
r.selection_glyph = Circle(fill_color="turquoise", line_color=None, fill_alpha=0.65)
r.nonselection_glyph = Circle(fill_color=None, line_color=None, fill_alpha=0.25)
#I made sure to use light colours for consistency.

#The reason the arguments in this grid plot is like this, is because a 2*2 grid html is  better to look at than a 1*4 line of graphs
p = gridplot([[p1, p2],[p3,p4]])
#shows graph ( ° ͜ʖ °)
show(p)

