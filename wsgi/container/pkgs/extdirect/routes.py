from . import bp
import flask


@bp.route('/models')
def index():
    return 'extjs model specs'
