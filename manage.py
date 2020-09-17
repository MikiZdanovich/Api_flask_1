import os

from flask_script import Manager


from backend.app import create_app, metadata


application = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')



manager = Manager(application)


@manager.command
def run():
    application.run()


@manager.command
def create_db():
    metadata.drop_all()
    metadata.create_all()


if __name__ == '__main__':
    metadata.drop_all()
    metadata.create_all()
    application.run()
