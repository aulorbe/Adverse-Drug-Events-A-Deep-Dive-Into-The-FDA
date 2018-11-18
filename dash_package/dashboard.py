from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.models import *
from dash_package.routes import *
from dash_package.queries import *
from dash.dependencies import Input, Output


# HOW OUR DASHBOARD WILL LOOK:
app.layout = html.Div(children=[
    html.H1(id = 'test , ''Most Deadly Drugs'),

    html.Div('''
        What FDA approved drugs where the deadliest?
    '''),
    html.P('lala'),

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
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
            id='class-dropdown',
            options=[
                {'label': 'New York City', 'value':'NYC'},
                {'label': u'Montréal', 'value': 'MTL'}
                ],
            value= ['NYC','MTL'],
            multi=True
            ),



    dcc.Tabs(
        id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
        ]),
    html.Div(id='tabs-content')




])

# @app.callback(
#     Output(component_id = 'example-graph', component_property='options'),
#     [Input(component_id='test', component_property='value')]
# def test():
