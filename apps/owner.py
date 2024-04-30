# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:33:47 2024

@author: Dabas
"""
import dash
import dash_html_components as html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import plotly.graph_objs as go

import plotly.express as px
import pandas as pd
import numpy as np

import plotly.express as px
from app import app
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
data = data_cleaned.dropna(subset=['Price'])


ownership_by_state = data.groupby(['Location', 'Owner_Type']).size().unstack(fill_value=0).reset_index()

layout = html.Div([
    html.H1("Ownership by State"),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': state, 'value': state} for state in ownership_by_state['Location']],
        value=ownership_by_state['Location'].iloc[0],  
        clearable=False
    ),
    dcc.Graph(
        id='ownership-by-state-bar-plot',
        config={'displayModeBar': True},
        style={'height': '800px'},
    )
])


@app.callback(
    Output('ownership-by-state-bar-plot', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_bar_plot(selected_state):
    filtered_data = ownership_by_state[ownership_by_state['Location'] == selected_state]
    if not filtered_data.empty:
        owner_types = filtered_data.columns[1:]
        counts = filtered_data.values[0][1:]
        
        
        colors = ['rgb(0, 102, 204)', 'rgb(0, 204, 102)', 'rgb(255, 128, 0)', 'rgb(255, 0, 0)']
        
       
        trace = go.Bar(
            y=owner_types,
            x=counts,
            orientation='h', 
            marker=dict(color=colors),
            hoverinfo='x+text',  
            text=counts,
            textposition='outside',  
        )
        
        layout = dict(
            title=f"Ownership by State: {selected_state}",
            xaxis=dict(title='Count'),
            yaxis=dict(title='Owner Type', tickangle=-45),
            plot_bgcolor='#f5f5f5',  
            paper_bgcolor='#f5f5f5',  
            font=dict(color='#333333'), 
            margin=dict(l=150, r=20, t=40, b=80),  
        )
        
        return {'data': [trace], 'layout': layout}
    else:
        return {'data': [], 'layout': {}}

app.layout = layout