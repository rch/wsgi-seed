from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from local.genshi import Genshi
import utils

app = Flask(__name__)

app.config.from_object('container.conf')

db = SQLAlchemy(app)

genshi = Genshi(app)

wrk = utils.make_celery(app)

# final reference
import container.main as main
main.register_blueprints(app)
