import sys
from flask import request
from sqlalchemy import select
from models.address import addressModel
from helpers import Encrypt, Serializer

class AddressController():

    @staticmethod
    def getAll():
        address = addressModel.findAll(select(addressModel))
        return Serializer.serialize_list(address)

    @staticmethod
    def get(id=None):
        address = addressModel.findOne(addressModel.id, id)
        return Serializer.serialize(address)

    
    @staticmethod
    def post():
        content = request.json
        address = addressModel(address=content['address'])
        address.create()

        return {
            "created": True,
        }