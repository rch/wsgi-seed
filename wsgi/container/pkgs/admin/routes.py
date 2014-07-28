from . import bp
import flask
from flask import Blueprint, current_app, request, render_template
import container.local.genshi as genshi


@bp.route("/")
def index():
    return genshi.render_response('base-layout.html')


@bp.route("/base-aside.html")
def aside():
    return genshi.render_response('base-aside.html', method='partial')

@bp.route("/entries.json")
def entries():
    return flask.jsonify(entries=['one','two','three'])
