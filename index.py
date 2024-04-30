# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:29:13 2024

@author: Dabas
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
# import all pages in the app
from apps import location, transmission, fueltype, mileage, owner, home, engine



dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("location", href="/location"),
        dbc.DropdownMenuItem("fueltype", href="/fueltype"),
        dbc.DropdownMenuItem("mileage", href="/mileage"),
        dbc.DropdownMenuItem("ownertype", href="/owner"),
        dbc.DropdownMenuItem("Transmission Type", href="/transmission"),
        dbc.DropdownMenuItem("Engine Power", href="/engine"),
    ],
    nav = True,
    in_navbar = True,
    label = "Navigate to ",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/logo.jpg", height="100px")),
                        dbc.Col(dbc.NavbarBrand("Second hand Car Market", className="ml-2")),
                    ],
                    align="center",
                    
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/location':
        return location.layout
    elif pathname == '/transmission':
        return transmission.layout
    elif pathname == '/fueltype':
        return fueltype.layout
    elif pathname == '/mileage':
        return mileage.layout
    elif pathname == '/owner':
        return owner.layout
    elif pathname == '/engine':
        return engine.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(port=8099,debug=True)