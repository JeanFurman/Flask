from flask import Flask
from config import basedir
import os


def create_app():
    app = Flask(__name__, 
        template_folder=os.path.join(basedir, 'resources', 'templates'),
        static_folder=os.path.join(basedir, 'resources', 'static')
    )
    app.config['SECRET_KEY'] = 'testing'

    from app import routes
    routes.load(app)

    from app.filters import text_truncate, text_upper
    app.jinja_env.filters['text_truncate'] = text_truncate
    app.jinja_env.filters['text_upper'] = text_upper

    return app