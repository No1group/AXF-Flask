
from flask_migrate import MigrateCommand

from flask_script import Manager

from App import create_app

print('xxx')
app = create_app('develop')
manage = Manager(app=app)
manage.add_command("db", MigrateCommand)

if __name__ =='__mian__':
    manage.run()

