from flask import render_template
# from dash_package.models import Listing
from dash_package import server
import pdb
from dash_package.models import Brands


@server.route('/')
def render_apartments():
    brand = Brands.query.first()
    return brand.name

    # return render_template('index.html', apartments = apartments)
