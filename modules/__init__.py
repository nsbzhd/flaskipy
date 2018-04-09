# coding=utf-8
from flask import Flask, jsonify
from .posts import post_routes
from .users import user_routes
from flask_sqlalchemy import SQLAlchemy
from utils.db import connect_to_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurations
app.config.from_object('config')
# Database connection
connect_to_db(app)

@app.errorhandler(404)
def not_found(error):
    # return "Error Message: {0}".format(error)
    response = {
        'success': False,
        'message': "Error Message: {0}".format(error)
    }

    return jsonify(response), 404

# Routes Register
# register post routers
app.register_blueprint(post_routes)
app.register_blueprint(user_routes)
