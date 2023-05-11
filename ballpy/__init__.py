from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'welcome to ball.py'

    # register reptiles blueprint 
    from . import reptile 
    app.register_blueprint(reptile.bp)

    # return the app 
    return app