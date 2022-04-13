from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

# 注册管理命令
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
# 添加操作数据库命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
