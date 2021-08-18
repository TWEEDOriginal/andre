from flask import Flask,Blueprint


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]="heydream"#encrypt cookies n session data
    
    #import the blueprints to be registered
    from .views import views
    # from .auth import auth

    #register all blueprints created
    app.register_blueprint(views,url_prefix="/")
    
    return app