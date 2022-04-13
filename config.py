import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-be-best"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
    #                           "sqlite:///" + os.path.join(basedir,"app.db")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:laohulo0910.@127.0.0.1/flask_blog"
    SQLALCHEMY_TRACT_MODIFICATIONS = False
    ENV = "development"
    DEBUG = True

