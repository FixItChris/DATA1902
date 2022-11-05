'''
Production of Interactive Visualisation
SID: 520419832

This code is uses the bokeh library to develop and generate the interactive visualisation required for 
Stage 4 of the group project. The graph itself will compare the QS2023 overall scores against their
corresponding THE2020 overall scores, allowing the user to subset the data with other categorical
variables.

'''
import pandas as pd
import numpy as np
from bokeh.layouts import column, row
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select, CustomJS, Button 
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap

## Loading/cleaning data
df = pd.read_csv("integrated_dataset.csv")
df["QS2023 Overall Score"] = round(df["QS2023 Academic Reputation"]*0.4 + df["QS2023 Employer Reputation"]*0.1
        + df["QS2023 Faculty Student Ratio"]*0.2 + df["QS2023 Citations per Faculty"]*0.2
        + df["QS2023 International Faculty Ratio"]*0.05 + df["QS2023 International Student Ratio"]*0.05, 1)

df["QS2023 Overall Score"] = round(df["QS2023 Overall Score"], 2)


# Organising columns
cols = sorted(df.columns)
categorical_cols = [x for x in cols if df[x].dtype == object]
categorical_cols.remove("institution")
categorical_cols.remove("location")
numerical_cols = [x for x in cols if df[x].dtype == "float64"]

# Possible colours and sizes to use UPDATE
COLORS = Spectral5
N_COLORS = len(COLORS)

TOOLTIPS = [
    ("Name", "@institution"),
    ("Country", "@location"),
    ("x", "$x"),
    ("y", "$y"),
]

source = ColumnDataSource(df)

## Create figure and update figure (callback) functions
def create_figure():
    keywords = dict()

    # Setting range of values if categorical columns are chosen
    if x.value in categorical_cols:
        keywords['x_range'] = sorted(set(df[x.value].values))
    if y.value in categorical_cols:
        keywords['y_range'] = sorted(set(df[y.value].values))
    
    # Creation of figure
    p = figure(height=700, width=700, tools="pan,wheel_zoom,box_zoom,hover,reset",
               title="Comparison Between QS2023 & THE2020 Data", **keywords, tooltips=TOOLTIPS)
    
    # Sets axis labels
    p.xaxis.axis_label = x.value.title()
    p.yaxis.axis_label = y.value.title()

    if x.value in categorical_cols:
        p.xaxis.major_label_orientation = np.pi / 4
    
    # Update colours
    if color.value != 'None':
        colors = factor_cmap(color.value, palette=Spectral5, factors=df[color.value].unique())
    
    # Draw points
    if color.value != 'None':
        p.circle(x=x.value, y=y.value, color=colors, line_color="white", size=9,
                 alpha=0.6, hover_color='white', hover_alpha=0.5, source=source)
    else:
        p.circle(x=x.value, y=y.value, color="#31AADE", line_color="white", size=9,
                 alpha=0.6, hover_color='white', hover_alpha=0.5, source=source)

    
    return p


def update_figure(attr, old, new):
    layout.children[1] = create_figure()


# Menus for each option to change
x = Select(title='X-Axis', value='QS2023 Overall Score', options=numerical_cols)
x.on_change('value', update_figure)

y = Select(title='Y-Axis', value='THE2020 Overall Score', options=numerical_cols)
y.on_change('value', update_figure)

color = Select(title='Color', value='None', options=['None'] + categorical_cols)
color.on_change('value', update_figure)

# Placement of bokeh controls
controls = row(x, y, color, width=200)
layout = column(controls, create_figure())

curdoc().add_root(layout)
curdoc().title = "520419832 Visualisation"
