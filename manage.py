# from flask.cli import FlaskGroup

# from back import app#, User, db


# cli = FlaskGroup(app)


# @cli.command("create_db")
# def create_db():
#     print("db")


# @cli.command("seed_db")
# def seed_db():
#     print("db")


# if __name__ == "__main__":
#     cli()
# manage.py
from flask.cli import FlaskGroup
from back import create_app

# Create the app using the factory function
app = create_app()

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    print("db")

@cli.command("seed_db")
def seed_db():
    print("db")

if __name__ == "__main__":
    cli()
