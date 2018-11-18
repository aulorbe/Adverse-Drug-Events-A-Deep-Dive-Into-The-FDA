from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash_package.models import *
from dash_package.routes import *
from dash_package.queries import *
from dash.dependencies import Input, Output


# HOW OUR DASHBOARD WILL LOOK:
app.layout = html.Div(children=[ # children of entire html page
    html.H1('An Exploration of the FDA\'s Adverse Events open API'), # title

    html.Br(), # line breaks
    html.Br(),
    html.Br(),

    dcc.Graph(
        id='graph-from-dropdown',
        # figure={
        #         'data': [
        #             {'x': [1, 2, 3], 'y': [5, 1, 2], 'type': 'bar', 'name': 'SF'},
        #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        #         ],
        #         'layout': {
        #             'title': 'Dash Data Visualization'
        #         }
            # }
            ),

    dcc.Dropdown( # our dropdown menu
        id = 'holiday-drop-down', # id referenced in routes.py function
        options=[{'label': i, 'value': i, 'display': 'block'} for i in ['Christmas', 'New Years']] # options for a list of two items: 'Christmas' and 'New Years'
    )


    # html.H3('An exploration of the FDA\'s Adverse Events open API'),

    #
    # dcc.Tabs(
    #     id="tabs", children=[
    #         dcc.Tab(id='tab 1', label='Men', children=[
    #             html.H3(children=''),
    #             dcc.Graph(id='men-graph',
    #                 figure={
    #                     'data': [
    #                         {'x': [1, 2, 3], 'y': [5, 1, 2], 'type': 'bar', 'name': 'SF'},
    #                         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #                     ],
    #                     'layout': {
    #                         'title': 'Total Adverse Events Effecting Men per 2017 Holiday'
    #                     }
    #                 }
    #             ),
    #         ]),
    #         dcc.Tab(label='Tab two', value='tab-2'),
    #     ]),


    # html.Div(id='tabs-content')




])

# @app.callback(
#     Output(component_id = 'example-graph', component_property='options'),
#     [Input(component_id='test', component_property='value')]
# def test():
