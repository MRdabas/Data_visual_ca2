# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:12:13 2024

@author: Dabas
"""

import dash
import dash_html_components as html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



import plotly.express as px
import pandas as pd
import numpy as np
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data_cleaned = data.drop(columns=['New_Price'])
cardata = data_cleaned.dropna(subset=['Price'])





from app import app

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
layout = html.Div([
    html.Div(style={'background-image': 'url("/assets/bg.jpg")',
                    'background-size': 'cover',
                    'background-position': 'center',
                    'height': '100vh'}, children=[
        dbc.Container([
            dbc.Row([
               
                dbc.Col(html.H1("Welcome to the Second Hand Car Sales dashboard", className="text-center"),
                        className="mb-5 mt-5")
            ]),
            dbc.Row([
                dbc.Col(html.H5(children='This app show the data from 6000 second car about the milage of car, Owner ship of car, Car model, location avalibality of car, Fuel type of car and all other important feature for car buying.'
                                 ),
                        className="mb-4")
            ]),

            dbc.Row([
                dbc.Col(html.H5(children='It consists of six main pages: The first show the availbility of car in each locations,  Next page page show the fueltype used in car '
                                         'The next page show the comparision of price of car with mileage give by each car, The next page contain the information about ownership of car, Next page show the Transmission Type of car from each location, Last but not list The comparison of price of car with the Engine cc of car we can filtter the data according to the years.'),
                        className="mb-5")
            ]),

            dbc.Row([
                dbc.Col(dbc.Card(children=[html.H3(children='Access the dataset from Kaggle',
                                                   className="text-center",
                                                   style = {'color': 'white'}),
                                            dbc.Button("Dataset",
                                                       href="https://www.kaggle.com/datasets/ayushparwal2026/cars-dataset?select=used_cars_data.csv",
                                                       color="primary",
                                                       className="mt-3",
                                                       style={'background-color': '#343a40', 'border-color': '#343a40', 'font-weight': 'bold'}),
                                                       
                                            ],
                                 body=True, color="dark", outline=True,
                                 style={'background-image': 'url("/assets/car1.jpg")',  
                                        'background-size': 'cover',
                                        'background-position': 'center',
                                        'margin-left': 'auto',  
                                        'margin-right': '0'})
                        , width=6, className="mb-4"),

            ], className="mb-5"),
            
            
        ])
    ])
])


app.layout = layout


