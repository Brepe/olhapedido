import os

from flask import (
    Flask,
    jsonify,
)
from model import models as md
from .views import main

# app = Flask(__name__)
# app.config.from_object("config.config.Config")


def create_app():
    app = Flask(__name__, template_folder="../templates")
    #app.run(host="0.0.0.0", port=5000)  # Add this line to start the app
    # Register the Blueprint
    app.register_blueprint(main)

    return app

# @app.route("/")
# def hello_world():
#     return jsonify(hello="world")

# @app.route("/db")
# def hello_db():
#     return jsonify(result)


# @app.route("/static/<path:filename>")
# def staticfiles(filename):
#     return send_from_directory(app.config["STATIC_FOLDER"], filename)


# @app.route("/media/<path:filename>")
# def mediafiles(filename):
#     return send_from_directory(app.config["MEDIA_FOLDER"], filename)


# @app.route("/upload", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         file = request.files["file"]
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
#     return """
#     <!doctype html>
#     <title>upload new File</title>
#     <form action="" method=post enctype=multipart/form-data>
#       <p><input type=file name=file><input type=submit value=Upload>
#     </form>
#     """
