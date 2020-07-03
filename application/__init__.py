from flask import Flask

from flask_apscheduler import APScheduler

scheduler = APScheduler()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object("config.ConfigDev")

    scheduler.init_app(app)
    scheduler.start()

    with app.app_context():

        from . import sms
        app.register_blueprint(sms.sms_bp)

        from . import services
        app.register_blueprint(services.services_bp)

        return app