import os

from flask_script import Manager

from backend.app import create_app, metadata
from backend.app.views import employee_bp

application = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
application.register_blueprint(employee_bp)


application.app_context().push()

manager = Manager(application)


@manager.command
def run():
    application.run()


@manager.command
def create_db():
    metadata.drop_all()
    metadata.create_all()


if __name__ == '__main__':
    manager.run()
