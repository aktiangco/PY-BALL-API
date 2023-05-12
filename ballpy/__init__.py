from flask import Flask, redirect
from flask_migrate import Migrate

#* for .env to work
from dotenv import load_dotenv
import os
load_dotenv()

POSTGRES = os.environ.get("POSTGRES") #to fetch from .env file

# factory
def create_app():
    app = Flask(__name__)
    
     # Database Config
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # to access to all built-in SQLAlchemy
    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return redirect('/reptiles')

    # register reptiles blueprint 
    from . import reptile 
    app.register_blueprint(reptile.bp)

    # return the app 
    return app