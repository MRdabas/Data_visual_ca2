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
from app import app


import plotly.express as px
import pandas as pd


import plotly.express as px
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
data = data_cleaned.dropna(subset=['Price'])


transmission_counts_by_location = data.groupby(['Location', 'Transmission']).size().unstack(fill_value=0)



layout = html.Div( children=[
    html.H1("Distribution of Automatic and Manual Transmissions by Location"),
    dcc.Graph(
        id='transmission-by-location-bar-chart',
        style={'height': '800px'},
        figure={
            'data': [
                {'x': transmission_counts_by_location.index, 'y': transmission_counts_by_location['Automatic'], 'type': 'bar', 'name': 'Automatic', 'marker': {'color': '#0095A8'}, 'width': 0.4},  # Orange
                {'x': transmission_counts_by_location.index, 'y': transmission_counts_by_location['Manual'], 'type': 'bar', 'name': 'Manual', 'marker': {'color': '#8B0000'}, 'width': 0.4}  # Cyan
            ],
            'layout': {
                'title': 'Automatic and Manual Transmissions by Location',
                'xaxis': {'title': 'Location'},
                'yaxis': {'title': 'Number of Cars'},
                'barmode': 'group',  
                'plot_bgcolor': '#f5f5f5',  # Background color
                #'paper_bgcolor': '#f5f5f5',  # Paper color
                'font': {'color': '#333333'}  # Font color
            }
        }
    )
])



app.layout = layout