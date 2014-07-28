import flask, container
import container.local.genshi as genshi
from flask import Blueprint, current_app, request, render_template
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

engine = create_engine('sqlite:///admin.db', echo=container.conf.DEBUG)

Base = declarative_base()

# finally
import model, routes
