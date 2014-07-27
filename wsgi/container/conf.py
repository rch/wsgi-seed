import os, sys
DEBUG = True
SECRET_KEY = 'FIXME_SECRET'
try:
    FREEZER_DESTINATION = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'frozen')
except AttributeError:
    pass


# postgresql
DEFAULT = os.getenv('USER')
DB_HOST = os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST', 'localhost')
DB_PORT = os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT', 5432)
DB_USER = os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME', os.getenv('DB_USER', DEFAULT))
DB_PASS = os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD', os.getenv('DB_PASS', DEFAULT))
DB_NAME = os.getenv('OPENSHIFT_APP_NAME', os.getenv('DB_NAME', DEFAULT))

DATABASE = {
    'host': DB_HOST,
    'port': DB_PORT,
    'u': DB_USER,
    'pw': DB_PASS,
    'db': DB_NAME,
}
SQLALCHEMY_DATABASE_URI = 'postgresql://{u}:{pw}@{host}:{port}/{db}'.format(**DATABASE)

# postgresql broker/backend is for development only
BROKER_URL = 'sqla+postgresql://{u}:{pw}@{host}:{port}/{db}'.format(**DATABASE)
CELERY_RESULT_ENGINE_OPTIONS = {'echo': False}
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_BACKEND = 'db+postgresql://{u}:{pw}@{host}:{port}/{db}'.format(**DATABASE)
CELERY_RESULT_DB_TABLENAMES = {
    'task': 'flask_taskmeta',
    'group': 'flask_groupmeta',
}
