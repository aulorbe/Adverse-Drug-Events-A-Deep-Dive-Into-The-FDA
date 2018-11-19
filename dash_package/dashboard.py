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
    # html.Strong(html.H3 ('Introduction')),
    html.P('This web application allows users to explore a database comprising of adverse event information across select holidays in 2017. The database was made with information from the FDA\'s API Drug Adverse Event endpoint.'),
    html.Br(),
    html.Br(),


    dcc.Tabs(id="tabs", children=[

        dcc.Tab(id='Tab 1', label='Deaths and Suicides', children=[
            # html.H3(children='Deaths and Suicides per Holiday'),
            dcc.Graph(
                id='graph-from-dropdown',
                    ),
            dcc.Dropdown( # our dropdown menu
                id = 'holiday-drop-down', # id referenced in routes.py function
                options=[{'label': i, 'value': i, 'display': 'block'} for i in ['Deaths per holiday', 'Suicides per holiday', 'Attempted Suicides per Holidays']],
                value='Deaths per holiday'
                    )]),

        dcc.Tab(id='Tab 2', label='Drugs Analysis', children=[
            # html.H1(children='Drug Related Adverse Events'),
            html.Br(),
            dcc.Graph(
                id='top-five-reactions-pie',
                # value = 'Top Five Adverse Reactions in 2017'
                    ),
            dcc.Dropdown( # our dropdown menu
                id = 'top-five-reactions-drop-down', # id referenced in routes.py function
                options=[{'label': i, 'value': i, 'display': 'block'} for i in ['Top Five Adverse Reactions in 2017', 'Top Five Adverse Brands in 2017']],
                value='Top Five Adverse Reactions in 2017'
            )
        ]),

        dcc.Tab(id='Tab 3', label='Sex Breakdown', children=[
            html.Br(),

            dash_table.DataTable(
                id='sex-table',
                columns=[{'name': 'Male', 'id': 'col-male'}, {'name': 'Female', 'id': 'col-female'}],
                style_header={
                                 'backgroundColor': '#FDEAEA',
                                 'fontWeight': 'bold',
                                 'color': 'black'
                                 }
                ),

            html.Br(),
            html.Br(),
            html.P('Pick a holiday from the dropdown menu below to see the breakdown of men v. women for that particular date.'),
            html.Br(),

            dcc.Dropdown(
                id='sex-dropdown',
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
                value="xmas"
                ),
        ])

    ])

])

@app.callback(Output('sex-table', 'data'),
                [Input('sex-dropdown', 'value')])
def sex_stats_per_holiday(value):
    if value == 'xmas':
        return [{'col-male': male_events_in_one_holiday('Christmas'),'col-female':female_events_in_one_holiday('Christmas')}]
    elif value =='tkgiving':
        return [{'col-male': male_events_in_one_holiday('Thanksgiving'),'col-female':female_events_in_one_holiday('Thanksgiving')}]
    elif value == 'halloween':
        return [{'col-male':male_events_in_one_holiday('Halloween'),'col-female':female_events_in_one_holiday('Halloween')}]
    elif value == 'NYE':
        return [{'col-male':male_events_in_one_holiday('New Years Eve'),'col-female':female_events_in_one_holiday('New Years Eve')}]
    elif value == 'vday':
        return [{'col-male':male_events_in_one_holiday('Valentine\'s Day'),'col-female':female_events_in_one_holiday('Valentine\'s Day')}]
    elif value == 'mardigras':
        return [{'col-male':male_events_in_one_holiday('Mardi Gras'),'col-female':female_events_in_one_holiday('Mardi Gras')}]
    elif value == '420':
        return [{'col-male':male_events_in_one_holiday('Cannabis Day'),'col-female':female_events_in_one_holiday('Cannabis Day')}]
    elif value == 'cinco':
        return [{'col-male':male_events_in_one_holiday('Cinco de Mayo'),'col-female':female_events_in_one_holiday('Cinco de Mayo')}]
    elif value == 'fourth':
        return [{'col-male':male_events_in_one_holiday('Independence Day'),'col-female':female_events_in_one_holiday('Independence Day')}]



#



@app.callback(Output('graph-from-dropdown', 'figure'), # output a graph
              [Input('holiday-drop-down', 'value')]) # our function render_content (below) will take as an input a value from the dropdown menu in the dashboard.py file.
def render_content(value): #we pass in a value from the dropdown menu in dashboard.py
    if value == 'Deaths per holiday': #if the value is 'Christmas', then we create a dictionary of parameters to fill in the graph whose id is 'graph from dropdown' in dashboard.py
        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [deaths_per_holiday('Christmas'), deaths_per_holiday('Thanksgiving'), deaths_per_holiday('Halloween'), deaths_per_holiday('Independence Day'), deaths_per_holiday('Cinco de Mayo'), deaths_per_holiday('Cannabis Day'), deaths_per_holiday('Mardi Gras'), deaths_per_holiday('Valentine\'s Day'), deaths_per_holiday('New Years Eve')], 'type': 'bar', 'name': 'SF'},
                ],
        'layout': {
            'title': 'Deaths per Holiday in 2017'
            }
            }
    elif value == 'Suicides per holiday':

        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [suicides_per_holiday('Christmas'), suicides_per_holiday('Thanksgiving'), suicides_per_holiday('Halloween'), suicides_per_holiday('Independence Day'), suicides_per_holiday('Cinco de Mayo'), suicides_per_holiday('Cannabis Day'), suicides_per_holiday('Mardi Gras'), suicides_per_holiday('Valentine\'s Day'), suicides_per_holiday('New Years Eve')], 'type': 'bar', 'name': 'SF'},
                ],
        'layout': {
            'title': 'Suicides per holiday'}}

    elif value == 'Attempted Suicides per Holidays':

        x = [x[0] for x in db.session.query(Holidays.name).all()]
        # y = [x[0] for x in ]
        return {'data': [
                {'x': x, 'y': [attempted_suicides_per_holiday('Christmas'), attempted_suicides_per_holiday('Thanksgiving'), attempted_suicides_per_holiday('Halloween'), attempted_suicides_per_holiday('Independence Day'), attempted_suicides_per_holiday('Cinco de Mayo'), attempted_suicides_per_holiday('Cannabis Day'), attempted_suicides_per_holiday('Mardi Gras'), attempted_suicides_per_holiday('Valentine\'s Day'), attempted_suicides_per_holiday('New Years Eve')], 'type': 'bar', 'name': 'SF'},
                ],
        'layout': {
            'title': 'Attempted Suicides per Holidays'}}

    else:
        return None




@app.callback(Output('top-five-reactions-pie', 'figure'),
    [Input('top-five-reactions-drop-down', 'value')])

def top_five_reactions_per_holiday(value):
    # if value == 'Top Five Adverse Reactions in 2017':
    if value == 'Top Five Adverse Reactions in 2017':
        layout = go.Layout(
            title='Top Five Adverse Reactions Reported During Adverse Events',
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
            title='Top Five Brand Drugs Involved With Adverse Events',
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




        # return None # else return nothing (but automatically defaults to outputting a graph because of our decorator so just outputs a blank graph)
