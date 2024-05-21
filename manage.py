from flask.cli import FlaskGroup

from back import app#, User, db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    print("db")


@cli.command("seed_db")
def seed_db():
    print("db")


if __name__ == "__main__":
    cli()
