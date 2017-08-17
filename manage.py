#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flaskwebdev import app, db, Role, User, mail

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('serv', Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User, mail=mail)


if __name__ == '__main__':
    manager.run()
