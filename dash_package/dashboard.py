import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from dash_package.__init__ import app, db
from dash_package.models import *
from dash_package.routes import *
from dash_package.queries import *


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


@app.callback(Output('graph-from-dropdown', 'figure'), # output a graph
              [Input('holiday-drop-down', 'value')]) # our function render_content (below) will take as an input a value from the dropdown menu in the dashboard.py file.
def render_content(value): #we pass in a value from the dropdown menu in dashboard.py
    if value == 'Christmas': #if the value is 'Christmas', then we create a dictionary of parameters to fill in the graph whose id is 'graph from dropdown' in dashboard.py
        x = [x[0] for x in db.session.query(Holidays.name).all()]
        return {'data': [
                {'x': x, 'y': [5, 1, 2, 1, 1, 1, 1, 1, 1], 'type': 'bar', 'name': 'SF'},
                ],
        'layout': {
            'title': 'Deaths per Holiday, 2017'
            }
            }
    else:
        return None # else return nothing (but automatically defaults to outputting a graph because of our decorator so just outputs a blank graph)
