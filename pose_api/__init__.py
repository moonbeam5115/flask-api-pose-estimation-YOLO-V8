import os
from flask import Flask, render_template, url_for, g
from pose_api.database import init_db, db_session


# Flask Application Factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'calendar_app.sqlite')
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize Database
    init_db()

    @app.teardown_appcontext
    def shudown_sesssion(exception=None):
        db_session.remove()

    # Register Blueprints (BP)
    # ------------------------
    # image_pose_estimation BP
    from pose_api.blueprints.home import home
    app.register_blueprint(home.bp)

    from pose_api.blueprints.image_pose_estimation import image_pose_estimation
    app.register_blueprint(image_pose_estimation.bp)

    return app