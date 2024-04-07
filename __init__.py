from flask import Flask
from flask_assets import Environment, Bundle
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URL', '').replace("postgres://", "postgresql://") or \
                                        os.environ.get('DATABASE_URL') or \
                                        'sqlite:///' + os.path.join(basedir, 'app.db')

assets = Environment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# bundles - dynamically load all files in css & js files
css_files = [str(path.relative_to('static')) for path in Path('static/css').rglob('*.css')]
css = Bundle(*css_files, output='gen/packed.css')
assets.register('css_all', css)

# could potentially include jQuery & bootstrap.js in here
js_files = [str(path.relative_to('static')) for path in Path('static/js').rglob('*.js')]
js = Bundle(*js_files, output='gen/packed.js')
assets.register('js_all', js)

# Import the Player model here
from .models import Player

# Move headers and conn initialization to a separate module
from . import routes  # Import views or routes
