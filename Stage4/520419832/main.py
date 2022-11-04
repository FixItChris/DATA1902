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
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Select, CustomJS, Div
from bokeh.palettes import Spectral5

## Loading/cleaning data
df = pd.read_csv("integrated_dataset.csv")
df["QS2023 Overall Score"] = round(df["QS2023 Academic Reputation"]*0.4 + df["QS2023 Employer Reputation"]*0.1
        + df["QS2023 Faculty Student Ratio"]*0.2 + df["QS2023 Citations per Faculty"]*0.2
        + df["QS2023 International Faculty Ratio"]*0.05 + df["QS2023 International Student Ratio"]*0.05, 1)

df["QS2023 Overall Score"] = round(df["QS2023 Overall Score"], 2)
#print(df.columns)
#print(df["QS2023 Overall Score"])


#print(df.info)

# Organising columns
cols = sorted(df.columns)
categorical_cols = [x for x in cols if df[x].dtype == object]
numerical_cols = [x for x in cols if df[x].dtype == "float64"]

# Possible colours and sizes to use UPDATE
SIZES = list(range(6, 22, 3))
COLORS = Spectral5
N_SIZES = len(SIZES)
N_COLORS = len(COLORS)

## Create (new) figure and update figure functions - Credit to bryevdv on GitHub
def create_figure():
    keywords = dict()

    # Setting range of values if categorical columns are chosen
    if x.value in categorical_cols:
        keywords['x_range'] = sorted(set(df[x.value].values))
    if y.value in categorical_cols:
        keywords['y_range'] = sorted(set(df[y.value].values))
    
    # Creation of figure
    p = figure(height=600, width=800, tools='pan,box_zoom,hover,reset', 
               title="Comparison Between QS2023 & THE2020 Data", **keywords)
    
    # Sets axis labels
    p.xaxis.axis_label = x.value.title()
    p.yaxis.axis_label = y.value.title()

    if x.value in categorical_cols:
        p.xaxis.major_label_orientation = np.pi / 4
    
    # Update sizes
    sz = 9
    if size.value != 'None':
        if len(set(df[size.value])) > N_SIZES:
            groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
        else:
            groups = pd.Categorical(df[size.value])
        sz = [SIZES[xx] for xx in groups.codes]
    
    # Update colours
    c = "#31AADE"
    if color.value != 'None':
        if len(set(df[color.value])) > N_COLORS:
            groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
        else:
            groups = pd.Categorical(df[color.value])
        c = [COLORS[xx] for xx in groups.codes]
    
    # Draw points
    p.circle(x=df[x.value].values, y=df[y.value].values, color=c, size=sz, line_color="white", alpha=0.6,
             hover_color='white', hover_alpha=0.5)

    return p


def update_figure(attr, old, new):
    layout.children[1] = create_figure()


# Menus for each option to change
x = Select(title='X-Axis', value='QS2023 Overall Score', options=cols)
x.on_change('value', update_figure)

y = Select(title='Y-Axis', value='THE2020 Overall Score', options=cols)
y.on_change('value', update_figure)

size = Select(title='Size', value='None', options=['None'] + numerical_cols)
size.on_change('value', update_figure)

color = Select(title='Color', value='None', options=['None'] + numerical_cols)
color.on_change('value', update_figure)


# Placement of bokeh controls
controls = column(x, y, color, size, width=200)
layout = row(controls, create_figure())

#p = create_figure()
show(layout)

curdoc().add_root(layout)
curdoc().title = "520419832"

'''# Graphing x,y
source = ColumnDataSource(df)
p = figure(title="520419832", x_axis_label="x", y_axis_label="y")

points = p.circle(x="QS2023 Overall Score", y="THE2020 Overall Score", source=source)
'''

'''## Widgets
# Above text
div = Div(
        text="""
             <p>Select the categorical information to show</p>
             """,
        width=200,
        height=30,
)

# Buttons for categorical data
labels = ["Location", "Size", "Academic Focus", "Research Intensity", "Age"]
radio_button_group = RadioButtonGroup(labels=labels, active=0)

radio_button_group.js_on_click(CustomJS(code="""
    console.log('radio_group: active=' + this.active, this.toString())
"""))

show(p)
show(radio_button_group)'''
