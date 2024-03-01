import sys
from flask import request
from sqlalchemy import select
from models.user import UserModel
from helpers import Encrypt, Serializer

class UserController():

    @staticmethod
    def getAll():
        users = UserModel.findAll(select(UserModel))
        return Serializer.serialize_list(users)

    @staticmethod
    def get(id=None):
        user = UserModel.findOne(UserModel.id, id)
        return Serializer.serialize(user)

    
    @staticmethod
    def post():
        content = request.json
        password = Encrypt.encrypt(content["password"])
        user = UserModel(name=content['name'], password=password, email=content['email'])
        user.create()

        return {
            "created": True,
        }