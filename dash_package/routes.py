
# needed for routes/queries to show up online
from flask import render_template, jsonify, json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from dash_package.__init__ import app, db
from dash_package.models import *
from dash_package.dashboard import *
from dash_package import server
from dash_package.queries import *

#needed for routes/queries to run
from sqlalchemy import create_engine, func, or_
from sqlalchemy.orm import sessionmaker
import numpy as np
import operator

@server.route('/q')
def render_view():
    hello = percent_men_and_women_across_all_events()
    return str(hello) #gets brand names only
