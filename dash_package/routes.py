
# needed for queries to show up online
from flask import render_template, jsonify, json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from dash_package.__init__ import app
from dash_package.models import *
import dash_package.dashboard

#needed for queries
from sqlalchemy import create_engine, func, or_
from dash_package.models import Adverse_Events, Brands, Brands_Events, Reactions, Reactions_Events, Holidays
from sqlalchemy.orm import sessionmaker
import numpy as np
import operator
from dash_package import db

# routes
@app.server.route('/')
def render_apartments():
    brand = Brands.query.first()
    return brand.name
