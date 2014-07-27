import os, flask, utils
from flask import Response, url_for, render_template, current_app, make_response
from datetime import datetime, timedelta
from container import app, routes


def register_blueprints(app, mapping=None):
    from container import pkgs
    app.register_blueprint(pkgs.admin.bp, url_prefix='/admin')
    app.register_blueprint(pkgs.angular.bp, url_prefix='/angular')
    app.register_blueprint(pkgs.bootstrap.bp, url_prefix='/bootstrap')
    app.register_blueprint(pkgs.common.bp, url_prefix='/common')
    app.register_blueprint(pkgs.extdirect.bp, url_prefix='/extdirect')
    app.register_blueprint(pkgs.ngstrap.bp, url_prefix='/ngstrap')
