import sys
from flask import request
import jwt
from sqlalchemy import select
from config import SECRET_KEY
from helpers import Encrypt
from models.user import UserModel

class AuthController():

    @staticmethod 
    def login():
        try:
            data = request.json
            if not data:
                return {
                    "message": "Please provide user details",
                    "data": None,
                    "error": "Bad request"
                }, 400
            # validate input
            # is_validated = validate_email_and_password(data.get('email'), data.get('password'))
            # if is_validated is not True:
            #     return dict(message='Invalid data', data=None, error=is_validated), 400

            user = UserModel.findOne(UserModel.email, data["email"])
            passhash = Encrypt.encrypt(data['password'])
            if passhash != user.password:
                return {
                        "message": "password invalid",
                }, 400

            if user:
                try:
                    # token should expire after 24 hrs
                    token = jwt.encode(
                        {"user_id": user.id},
                        SECRET_KEY,
                        algorithm="HS256"
                    )
                    return {
                        "message": "Successfully fetched auth token",
                        # "data": user,
                        "token":token
                    }
                except Exception as e:
                    return {
                        "error": "Something went wrong",
                        "message": str(e)
                    }, 500
            return {
                "message": "Error fetching auth token!, invalid email or password",
                "data": None,
                "error": "Unauthorized"
            }, 404
        except Exception as e:
            return {
                    "message": "Something went wrong!",
                    "error": str(e),
                    "data": None
            }, 500