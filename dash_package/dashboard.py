import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from dash_package.__init__ import app, db
from dash_package.models import *
from dash_package.routes import *
from dash_package.queries import *
import plotly.graph_objs as go
import dash_table



# HOW OUR DASHBOARD WILL LOOK:
app.layout = html.Div(id='main', children = [
    html.H1('Beyond The FDA: Drug-Related Adverse Events in 2017'),
    html.Br(),


    # INTRODUCTORY TEXT
    html.P('This web application allows users to explore the adverse events reported to the FDA across select holidays in 2017. An adverse event is any symptom that occurs while taking a drug, which may or may not have been caused by the drug. Everything in the database was gathered by querying the FDA\'s openFDA drug adverse event API.'),
    html.P(html.Strong('Some observations of note:'),),
    html.Ul(children=[
        html.Li('The holiday with highest number of adverse events reported to the FDA was Cannabis Day (5,242).'),
        html.Li('Across all the holidays in this dataset, men made up 40.86% of total adverse events, while women made up 59.14% of total adverse events. We plan to do an age analysis at a later point.')
        ]
        ),
    html.P(html.Strong('Some questions we tried to answer with our app include:'),),
    html.Ul(children=[
        html.Li('What were the most common drugs involved with adverse events during the holidays?'),
        html.Li('What were the most common reactions reported during adverse sevents?'),
        html.Li('Which holidays had the most deaths, suicides, and attempted suicides?')
        ]
    ),
    html.Br(),

    # STARTING TABS SECTION
    dcc.Tabs(id="tabs", children=[

        # TAB 1
        dcc.Tab(id='Tab 1', label='Individual Holiday Statistics', children=[
            html.Br(),

            html.P('Pick a holiday from the menu below and its stats will appear below.'),
            html.Br(),

            # DROP DOWN TO POPULATE DATA TABLE
            dcc.Dropdown(
                id='stats-dropdown',
                options=[
                    {'label': 'Christmas', 'value': 'xmas'},
                    {'label': 'Thanksgiving', 'value': 'tkgiving'},
                    {'label': 'Halloween', 'value': 'halloween'},
                    {'label': 'New Years Eve', 'value': 'NYE'},
                    {'label': 'Valentine\'s Day', 'value': 'vday'},
                    {'label': 'Mardi Gras', 'value': 'mardigras'},
                    {'label': 'Cannabis Day', 'value': '420'},
                    {'label': 'Cinco de Mayo', 'value': 'cinco'},
                    {'label': 'Independence Day', 'value': 'fourth'},
                ],
                value="xmas",
                ),
            html.Br(),
            html.Br(),
            # DATA TABLE
            dash_table.DataTable(
                id='holiday_stats',
                columns=[{'name': 'Male', 'id': 'col-male'}, {'name': 'Female', 'id': 'col-female'}, {'name': 'Adverse Events', 'id': 'col-events'}],
                style_header={
                                 'backgroundColor': '#ADD8E6',
                                 'fontWeight': 'bold',
                                 'color': 'black'
                                 }
                ),


            html.Br(),
            dcc.Graph(
                id='top-five-brands-per-holiday-pie',
                # value = 'xmas'
                    ),
            html.Br(),
            dcc.Graph(
                id='top-five-reactions-per-holiday-pie',
                # value = 'xmas'
                    ),

            html.Br(),
            # DATA TABLE INSTRUCTIONS

            ]),

        # TAB 2
        dcc.Tab(id='Tab 2', label='Top 5 Brands & Reactions Associated With Adverse Events Across All Holidays', children=[
            # html.H1(children='Drug Related Adverse Events'),
            html.Br(),

            # PIE CHART
            dcc.Graph(
                id='top-five-reactions-pie',
                # value = 'Top Five Adverse Reactions in 2017'
                    ),
            # PIE CHART INSTRUCTIONS
            html.P('Pick a category from the menu below and the breakdown will appear above.'),
            html.Br(),

            # DROP DOWN MENU FOR PIE CHART
            dcc.Dropdown( # our dropdown menu
                id = 'top-five-reactions-drop-down', # id referenced in routes.py function
                options=[{'label': i, 'value': i, 'display': 'block'} for i in ['Top Five Adverse Reactions in 2017', 'Top Five Adverse Brands in 2017']],
                value='Top Five Adverse Reactions in 2017'
            )
        ]),

        # TAB 3
        dcc.Tab(id='Tab 3', label='Deaths and Suicides Across All Holidays', children=[
            # html.H3(children='Deaths and Suicides per Holiday'),

            # BAR CHART
            dcc.Graph(
                id='graph-from-dropdown',
                    ),

            # BAR CHART INSTRUCTIONS
            html.P('Pick a category from the menu below and its stats will appear in the chart above.'),
            html.Br(),

            # DROP DOWN FOR BAR CHART
            dcc.Dropdown( # our dropdown menu
                id = 'holiday-drop-down', # id referenced in routes.py function
                options=[{'label': i, 'value': i, 'display': 'block'} for i in ['Deaths per Holiday', 'Suicides per Holiday', 'Attempted Suicides per Holiday']],
                value='Deaths per Holiday'
                    ),
            html.Br(),

        ]),
        #Men Vs Women
        dcc.Tab(id='Tab 4', label='Gender Analysis', children=[
            # html.H3(children='Deaths and Suicides per Holiday'),

            # BAR CHART
            dcc.Graph(
                id='gender-graph-from-dropdown'
                    ),

            # BAR CHART INSTRUCTIONS
            html.P('Pick a category from the menu below and its stats will appear in the chart above.'),
            html.Br(),

            # DROP DOWN FOR BAR CHART
            dcc.Dropdown( # our dropdown menu
                id = 'gender-holiday-drop-down', # id referenced in routes.py function
                options=[
                    {'label': 'Christmas', 'value': 'xmas'},
                    {'label': 'Thanksgiving', 'value': 'tkgiving'},
                    {'label': 'Halloween', 'value': 'halloween'},
                    {'label': 'New Years Eve', 'value': 'NYE'},
                    {'label': 'Valentine\'s Day', 'value': 'vday'},
                    {'label': 'Mardi Gras', 'value': 'mardigras'},
                    {'label': 'Cannabis Day', 'value': '420'},
                    {'label': 'Cinco de Mayo', 'value': 'cinco'},
                    {'label': 'Independence Day', 'value': 'fourth'},
                ],
                value='xmas'
                    ),
            html.Br(),
        ])
    ])
])

# CALL BACKS / QUERIES
@app.callback(Output('holiday_stats', 'data'),
                [Input('stats-dropdown', 'value')])
def sex_stats_per_holiday(value):
    if value == 'xmas':
        return [{'col-male': male_events_in_one_holiday('Christmas'),'col-female':female_events_in_one_holiday('Christmas'), 'col-events': str(find_total_number_of_events_one_holiday('Christmas'))}]
    elif value =='tkgiving':
        return [{'col-male': male_events_in_one_holiday('Thanksgiving'),'col-female':female_events_in_one_holiday('Thanksgiving'), 'col-events': str(find_total_number_of_events_one_holiday('Thanksgiving'))}]
    elif value == 'halloween':
        return [{'col-male':male_events_in_one_holiday('Halloween'),'col-female':female_events_in_one_holiday('Halloween'), 'col-events': str(find_total_number_of_events_one_holiday('Halloween'))}]
    elif value == 'NYE':
        return [{'col-male':male_events_in_one_holiday('New Years Eve'),'col-female':female_events_in_one_holiday('New Years Eve'), 'col-events': str(find_total_number_of_events_one_holiday('New Years Eve'))}]
    elif value == 'vday':
        return [{'col-male':male_events_in_one_holiday('Valentine\'s Day'),'col-female':female_events_in_one_holiday('Valentine\'s Day'), 'col-events': str(find_total_number_of_events_one_holiday('Valentine\'s Day'))}]
    elif value == 'mardigras':
        return [{'col-male':male_events_in_one_holiday('Mardi Gras'),'col-female':female_events_in_one_holiday('Mardi Gras'), 'col-events': str(find_total_number_of_events_one_holiday('Mardi Gras'))}]
    elif value == '420':
        return [{'col-male':male_events_in_one_holiday('Cannabis Day'),'col-female':female_events_in_one_holiday('Cannabis Day'), 'col-events': str(find_total_number_of_events_one_holiday('Cannabis Day'))}]
    elif value == 'cinco':
        return [{'col-male':male_events_in_one_holiday('Cinco de Mayo'),'col-female':female_events_in_one_holiday('Cinco de Mayo'), 'col-events': str(find_total_number_of_events_one_holiday('Cinco de Mayo'))}]
    elif value == 'fourth':
        return [{'col-male':male_events_in_one_holiday('Independence Day'),'col-female':female_events_in_one_holiday('Independence Day'), 'col-events': str(find_total_number_of_events_one_holiday('Independence Day'))}]


@app.callback(Output('graph-from-dropdown', 'figure'), # output a graph
              [Input('holiday-drop-down', 'value')]) # our function render_content (below) will take as an input a value from the dropdown menu in the dashboard.py file.
def render_content(value): #we pass in a value from the dropdown menu in dashboard.py
    if value == 'Deaths per Holiday': #if the value is 'Christmas', then we create a dictionary of parameters to fill in the graph whose id is 'graph from dropdown' in dashboard.py
        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [deaths_per_holiday('Christmas'), deaths_per_holiday('Thanksgiving'), deaths_per_holiday('Halloween'), deaths_per_holiday('Independence Day'), deaths_per_holiday('Cinco de Mayo'), deaths_per_holiday('Cannabis Day'), deaths_per_holiday('Mardi Gras'), deaths_per_holiday('Valentine\'s Day'), deaths_per_holiday('New Years Eve')], 'type': 'bar'},
                ],
        'layout': {
            'title': 'Deaths per Holiday in 2017'
            }
            }
    elif value == 'Suicides per Holiday':

        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [suicides_per_holiday('Christmas'), suicides_per_holiday('Thanksgiving'), suicides_per_holiday('Halloween'), suicides_per_holiday('Independence Day'), suicides_per_holiday('Cinco de Mayo'), suicides_per_holiday('Cannabis Day'), suicides_per_holiday('Mardi Gras'), suicides_per_holiday('Valentine\'s Day'), suicides_per_holiday('New Years Eve')], 'type': 'bar'},
                ],
        'layout': {
            'title': 'Suicides per Holiday'}}

    elif value == 'Attempted Suicides per Holiday':

        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [attempted_suicides_per_holiday('Christmas'), attempted_suicides_per_holiday('Thanksgiving'), attempted_suicides_per_holiday('Halloween'), attempted_suicides_per_holiday('Independence Day'), attempted_suicides_per_holiday('Cinco de Mayo'), attempted_suicides_per_holiday('Cannabis Day'), attempted_suicides_per_holiday('Mardi Gras'), attempted_suicides_per_holiday('Valentine\'s Day'), attempted_suicides_per_holiday('New Years Eve')], 'type': 'bar'},
                ],
        'layout': {
            'title': 'Attempted Suicides per Holiday'}}

    else:
        return None


@app.callback(Output('top-five-reactions-pie', 'figure'),
    [Input('top-five-reactions-drop-down', 'value')])

def top_five_reactions_across_holidays(value):
    # if value == 'Top Five Adverse Reactions in 2017':
    if value == 'Top Five Adverse Reactions in 2017':
        layout = go.Layout(
            # title='Top Five Adverse Reactions Reported During Adverse Events',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction[0] for reaction in top_five_most_common_reactions()],
                values=[reaction[1] for reaction in top_five_most_common_reactions()],
                # text=['title']
                # hoverinfo='text',
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)

    elif value == 'Top Five Adverse Brands in 2017':
        layout = go.Layout(
            # title='Top Five Brand Drugs Involved With Adverse Events',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[brand[0] for brand in top_five_most_common_brands()],
                values=[brand[1] for brand in top_five_most_common_brands()],
                # text=['title']
                # hoverinfo='text',
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)


@app.callback(Output('top-five-brands-per-holiday-pie', 'figure'),
    [Input('stats-dropdown', 'value')])
def top_five_reactions_per_holiday(value):
    if value == 'xmas':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Christmas 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Christmas')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Christmas')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'tkgiving':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Thanksgiving 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Thanksgiving')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Thanksgiving')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'halloween':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Halloween 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Halloween')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Halloween')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'NYE':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for New Years Eve 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('New Years Eve')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('New Years Eve')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'vday':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Valentine\'s Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Valentine\'s Day')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Valentine\'s Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'mardigras':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Mardi Gras 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Mardi Gras')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Mardi Gras')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == '420':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Cannabis Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Cannabis Day')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Cannabis Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'cinco':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Cinco de Mayo 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Cinco de Mayo')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Cinco de Mayo')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'fourth':
        layout = go.Layout(
            title='Top Five Brand Drugs Associated with Adverse Events for Independence Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_brands_names_in_one_holiday('Independence Day')],
                values=[reaction for reaction in top_five_brands_count_in_one_holiday('Independence Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    else:
        return None


# INDIVIDUAL HOLIDAY REACTIONS PIES
@app.callback(Output('top-five-reactions-per-holiday-pie', 'figure'),
    [Input('stats-dropdown', 'value')])
def top_five_reactions_per_holiday(value):
    if value == 'xmas':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Christmas 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Christmas')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Christmas')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'tkgiving':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Thanksgiving 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Thanksgiving')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Thanksgiving')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'halloween':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Halloween 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Halloween')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Halloween')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'NYE':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for New Years Eve 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('New Years Eve')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('New Years Eve')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'vday':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Valentine\'s Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Valentine\'s Day')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Valentine\'s Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'mardigras':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Mardi Gras 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Mardi Gras')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Mardi Gras')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == '420':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Cannabis Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Cannabis Day')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Cannabis Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'cinco':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Cinco de Mayo 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Cinco de Mayo')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Cinco de Mayo')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    elif value == 'fourth':
        layout = go.Layout(
            title='Top Five Reactions Reported During Adverse Events for Independence Day 2017',
            showlegend=False,
            margin=go.Margin(l=50, r=50, t=40, b=40)
            )
        pie = go.Pie(
                labels=[reaction for reaction in top_five_reaction_names_in_one_holiday('Independence Day')],
                values=[reaction for reaction in top_five_reactions_count_in_one_holiday('Independence Day')],
                textinfo="label+percent"
            )
        return go.Figure(data=[pie], layout=layout)
    else:
        return None


@app.callback(Output('gender-graph-from-dropdown', 'figure'), # output a graph
              [Input('gender-holiday-drop-down', 'value')]) # our function render_content (below) will take as an input a value from the dropdown menu in the dashboard.py file.
def render_content(value): #we pass in a value from the dropdown menu in dashboard.py
    # f = 'Female Events'
    # m = 'Male Events'
    if value == 'xmas': #if the value is 'Christmas', then we create a dictionary of parameters to fill in the graph whose id is 'graph from dropdown' in dashboard.py
        # y = [x[0] for x in ]
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Christmas')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Christmas')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'tkgiving':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Thanksgiving')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Thanksgiving')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'halloween':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Halloween')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Halloween')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'NYE':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('New Years Eve')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('New Years Eve')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'vday':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Valentine\'s Day')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Valentine\'s Day')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'mardigras':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Mardi Gras')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Mardi Gras')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == '420':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Cannabis Day')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Cannabis Day')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'cinco':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Cinco de Mayo')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Cinco de Mayo')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }
    elif value == 'fourth':
        return {'data': [
                {'x': ['Female Events'], 'y': [female_events_in_one_holiday('Independence Day')], 'type': 'bar'},
                {'x': ['Male Events'], 'y': [male_events_in_one_holiday('Independence Day')], 'type': 'bar'}
                ],
        'layout': {
            'title': 'Gender Analysis per Holiday',
            'showlegend':False
            }
            }

    else:
        return None




{'label': 'Cinco de Mayo', 'value': 'cinco'},
{'label': 'Independence Day', 'value': 'fourth'}
