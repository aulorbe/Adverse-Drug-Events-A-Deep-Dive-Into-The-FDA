
from flask import Flask

import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///adverse-events.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True


from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy(server)


app = dash.Dash(__name__, server=server, url_base_pathname='/')



from dash_package.dashboard import *
from dash_package.routes import *
from dash_package.dashboard import *
