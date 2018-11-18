
from flask import render_template, jsonify, json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from dash_package.__init__ import app
from dash_package.models import *
import dash_package.dashboard







@app.server.route('/')
def render_apartments():
    brand = Brands.query.first()
    return brand.name
