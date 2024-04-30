
import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from dash import dcc, html, Input, Output
import plotly.graph_objs as go
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
data = data_cleaned.dropna(subset=['Price'])
data['Price'] *= 100000
from app import app
locations = data['Location'].unique()
layout = html.Div([
    html.H1("Car Price by Year"),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': loc, 'value': loc} for loc in locations],
        value=locations[0],  
        clearable=False
    ),
    dcc.Graph(
        id='price-by-year-scatter-plot',
        config={'displayModeBar': False},  
        style={'height': '800px'}  
    )
])


@app.callback(
    Output('price-by-year-scatter-plot', 'figure'),
    [Input('location-dropdown', 'value')]
)
def update_scatter_plot(selected_location):
    filtered_data = data[data['Location'] == selected_location]
    trace = go.Scatter(
        x=filtered_data['Year'],
        y=filtered_data['Price'],
        mode='markers',
        marker=dict(
            size=10,
            color='blue',  
            opacity=0.7,
            line=dict(width=0.5, color='black')  
        ),
        text=filtered_data['Name'],  
        hoverinfo='text+y'  
    )
    layout = dict(
        title=f"Car Price by Year in {selected_location}",
        xaxis=dict(title='Year'),
        yaxis=dict(title='Price (INR)', tickmode='linear', tick0=0, dtick=250000, range=[0, 2000000]), 
        plot_bgcolor='#f5f5f5',  
        paper_bgcolor='#f5f5f5', 
        font=dict(color='#333333')  
    )
    return {'data': [trace], 'layout': layout}

app.layout = layout