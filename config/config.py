import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    pg_host = os.getenv("SQL_HOST")
    pg_user = os.getenv("POSTGRES_USER")
    pg_pass = os.getenv("POSTGRES_PASSWORD")
    pg_db = os.getenv("POSTGRES_DB")
    #SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/service/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/service/media"
