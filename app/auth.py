from flask import Blueprint, jsonify, request
from app.models import User
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)

@bp.route('/signin', methods=['POST'])
def signin():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)