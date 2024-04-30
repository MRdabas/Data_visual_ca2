import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Read data
data = pd.read_csv("D:/dkit/datavisvilization/used_cars_data.csv")
data['Engine'] = data['Engine'].str.replace('CC', '').astype(float).astype(pd.Int64Dtype())


data = data[data['Engine'].notna() & (data['Engine'] != 0)]
data['Price'] *= 100000

data['Engine'] = data['Engine'].astype(int)


from app import app
# Define colors
colors = {
    'background': '#f5f5f5',
    'text': '#333333',
    'plot_color': '#009688' 
}


layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Engine Size vs Price',
            style={'textAlign': 'center', 'color': colors['text']}
    ),
    dcc.Graph(id='scatter-plot'),
    html.Div(children=[
        dcc.Markdown('''
        **Instructions:**
        - Adjust the slider below to filter the data by year range.
        - Hover over the data points in the scatter plot to view more details.
        ''',
        style={'color': colors['text']}
        ),
        html.Label('Year Range', style={'color': colors['text']}),
        dcc.RangeSlider(
            id='year-slider',
            min=data['Year'].min(),
            max=data['Year'].max(),
            value=[data['Year'].min(), data['Year'].max()],
            marks={str(year): str(year) for year in range(data['Year'].min(), data['Year'].max() + 1)},
            step=None
        )
    ])
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('year-slider', 'value')]
)
def update_scatter_plot(year_range):
   
    filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]

    
    fig = px.scatter(filtered_data, x='Engine', y='Price', title='Engine vs Price',
                     color_discrete_sequence=[colors['plot_color']], hover_data=['Name'])

    # Update layout
    fig.update_layout(
        xaxis_title='Engine Size',
        yaxis_title='Price',
        plot_bgcolor=colors['background'],
        font=dict(color=colors['text'])
    )

    return fig
app.layout = layout
