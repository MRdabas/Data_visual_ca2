# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:33:13 2024

@author: Dabas
"""

import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd


from app import app
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
data = data_cleaned.dropna(subset=['Price'])
data['Price'] *= 100000
data = data.dropna(subset=['Mileage'])
data['Mileage'] = data['Mileage'].str.replace(' kmpl', '')
data['Mileage'] = data['Mileage'].str.replace(' km/kg', '').astype(float)
data = data[data['Mileage'] != 0]

locations = data['Location'].unique()


layout = html.Div([
    html.H1("Car Price vs. Mileage"),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': loc, 'value': loc} for loc in locations],
        value=locations[0],  
        clearable=False,
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(
        id='price-vs-mileage-scatter-plot',
        config={'displayModeBar': True},  
        style={'height': '800px'} 
    )
])

@app.callback(
    Output('price-vs-mileage-scatter-plot', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_scatter_plot(selected_location):
    filtered_data = data[data['Location'] == selected_location].sort_values(by='Mileage')
    trace = go.Scatter(
        x=filtered_data['Mileage'],
        y=filtered_data['Price'],
      
        mode='markers',
        marker=dict(
            size=15,
            color='rgb(255, 128, 0)',  
            opacity=0.7,
            line=dict(width=1, color='rgb(0, 0, 0)')  
        ),
        text=filtered_data.apply(lambda row: f"{row['Name']}<br>Fuel Type: {row['Fuel_Type']}<br>Mileage: {row['Mileage']:.1f} kmpl<br>Price: {row['Price']:.0f} INR", axis=1),  
   hoverinfo='text' 
    )
    layout = dict(
        title=f"Car Price vs. Mileage in {selected_location}",
        titlefont={'size': 24, 'color': '#333333'},  # Title font properties
        xaxis=dict(title='Mileage (kmpl)', tickmode='linear', tickfont={'size': 14, 'color': '#333333'}, tickvals=filtered_data['Mileage'], ticktext=[f'{mileage:.1f}' for mileage in filtered_data['Mileage']]),
        yaxis=dict(title='Price (INR)', tickmode='linear', tick0=0, dtick=500000, range=[0, 2000000], tickfont={'size': 14, 'color': '#333333'}), 
        plot_bgcolor='#f5f5f5',  
        paper_bgcolor='#f5f5f5', 
        font=dict(color='#333333')  
    )
    return {'data': [trace], 'layout': layout}


app.layout = layout
