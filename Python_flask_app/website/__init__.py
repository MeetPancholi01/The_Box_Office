from flask import Flask
import os

def create_app():
    app = Flask(__name__,static_url_path='/static')

    # from .views import views
    from .auth import auth
    # app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')

    app.config["SECRET_KEY"] = "njnjn jnjjndefem kfowko"
    package_dir = os.path.dirname(
    os.path.abspath(__file__)
    )
    static = os.path.join(
        package_dir, "static"
    )
    app.static_folder=static
    return app