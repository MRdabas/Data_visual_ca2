# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:33:33 2024

@author: Dabas
"""
import dash
import dash_html_components as html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Read data
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
data = data_cleaned.dropna(subset=['Price'])
locations = data['Location'].unique()
from app import app

# Define color and shape mappings for transmission types
transmission_color_map = {'Manual': '#0095A8', 'Automatic': '#8B0000'}
transmission_shape_map = {'Manual': 'circle', 'Automatic': 'square'}

# Define layout
layout = html.Div(children=[
    html.H1("Distribution of Transmission and Fuel Type by Location"),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': loc, 'value': loc} for loc in locations],
        value=locations[0],  # Default value
        clearable=False
    ),
    dcc.Graph(
        id='transmission-fueltype-bar-chart',
        style={'height': '800px'},
    )
])


@app.callback(
    Output('transmission-fueltype-bar-chart', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_bar_chart(selected_location):
   
    filtered_data = data[data['Location'] == selected_location]
    
    
    grouped_data = filtered_data.groupby(['Fuel_Type', 'Transmission']).size().reset_index(name='count')
   
    fig = px.bar(
        grouped_data,
        x='Fuel_Type',
        y='count',
        color='Transmission',
        barmode='group',
        title=f'Distribution of Transmission and Fuel Type in {selected_location}',
        labels={'Fuel_Type': 'Fuel Type', 'Transmission': 'Transmission', 'count': 'Number of Cars'},
        category_orders={'Transmission': ['Manual', 'Automatic']},
        height=600,
        text='count',  
        opacity=0.7,
        hover_data={'count': True},  
    )
    
    
    fig.update_layout(
        plot_bgcolor='#f5f5f5',  
        font=dict(color='#333333'),  
        xaxis=dict(title='Fuel Type'),
        yaxis=dict(title='Number of Cars')
    )
    
    return fig
app.layout = layout

