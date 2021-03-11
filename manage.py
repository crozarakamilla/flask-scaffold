import os

from app import create_app, db
from app.models import *
from flask_script import Manager, Shell

app = create_app(os.getenv('API_CONFIG') or 'default')
manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


if __name__ == '__main__':
    manager.run()
