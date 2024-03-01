import sys
from flask import request
from sqlalchemy import select
from models.address import addressModel
from helpers import Encrypt, Serializer
from models.status import statusModel

class AddressController():

    @staticmethod
    def getAll():
        address = addressModel.findAll(select(addressModel))
        response = Serializer.serialize_list(address)
        for add in response:
            add["active"] = statusModel.count_group_by(statusModel.address_id == add["id"], statusModel.status == True, statusModel.address_id) or 0
            add["inactive"] = statusModel.count_group_by(statusModel.address_id == add["id"], statusModel.status == False, statusModel.address_id) or 0

        return response

    @staticmethod
    def get(id=None):
        address = addressModel.findOne(addressModel.id, id)
        response = Serializer.serialize(address)
        response["active"] = statusModel.count_group_by(statusModel.address_id == response["id"], statusModel.status == True, statusModel.address_id) or 0
        response["inactive"] = statusModel.count_group_by(statusModel.address_id == response["id"], statusModel.status == False, statusModel.address_id) or 0

        return response

    
    @staticmethod
    def post():
        content = request.json
        address = addressModel(address=content['address'], name=content["name"])
        address.create()

        return {
            "created": True,
        }