#import numpy as np 
#import pandas as pd
import plotly.express as px
import plotly.offline as py
#import plotly.graph_objs as go
from plotly.figure_factory import create_table

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Display the first 15 rows as a table
table = create_table(gapminder.head(15))
py.plot(table)

# Filter data for India
india_data = gapminder.query("country == 'India'")

# Bar plot for India's population over the years
fig = px.bar(india_data, x='year', y='pop', height=400)
fig.show()

# Scatter plot for 2007 data
gap2007 = gapminder.query('year == 2007')
fig = px.scatter(gap2007, x='gdpPercap', y='lifeExp', height=400, color='continent', size='pop', size_max=30)
fig.show()

# Scatter plot with facets for 2007 data
fig = px.scatter(gap2007, x='gdpPercap', y='lifeExp', height=400, color='continent', size='pop', size_max=60, facet_col='continent')
fig.show()

# Animated scatter plot
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, hover_name='country',
                 log_x=True, animation_frame='year', height=500, animation_group='country', range_x=[25, 10000], range_y=[25, 90])
fig.show()

# Animated scatter plot with labels
fig = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent', size='pop', size_max=40, hover_name='country',
                 log_x=True, animation_frame='year', height=500, animation_group='country', range_x=[25, 10000], range_y=[25, 90],
                 labels={'pop': "Population", 'gdpPercap': "GDP Per Capita", 'lifeExp': "Life Expectancy"})
fig.show()

# Geo line plot for 2007 data
fig = px.line_geo(gapminder.query('year == 2007'), locations='iso_alpha', color='continent', projection='orthographic', hover_name='country')
fig.show()

# Geo scatter plot for 2007 data
fig = px.scatter_geo(gapminder.query('year == 2007'), height=500, locations='iso_alpha', color='continent', size='pop', size_max=30, projection='orthographic', hover_name='country')
fig.show()

# Choropleth map
fig = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', height=500, animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
fig.show()

# Display available templates
import plotly.io as pio
pio.templates

# Bar plot with different templates
templates = ['plotly_dark', 'seaborn', 'ggplot2']
for template in templates:
    fig = px.bar(india_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of India'}, height=400, template=template)
    fig.show()
