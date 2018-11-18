from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.models import *
from dash_package.routes import *
from dash_package.queries import *


christmas = find_total_number_of_events_one_holiday('Christmas')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app.layout = html.Div(children=[
    html.H1(children='Most Deadly Drugs'),

    html.Div(children='''
        What FDA approved drugs where the deadliest?
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [5, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
