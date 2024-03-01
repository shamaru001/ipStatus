import sys
from flask import request
from sqlalchemy import select
from models.status  import statusModel
from helpers import Encrypt, Serializer

class StatusController():

    @staticmethod
    def getAll():
        status = statusModel.findAll(select(statusModel))
        return Serializer.serialize_list(status)

    @staticmethod
    def get(address_id=None):
        status = statusModel.findOne(statusModel.address_id, address_id)
        return Serializer.serialize(status)

    
    # @staticmethod
    # def post():
    #     content = request.json
    #     status = statusModel(address_id=content['address_id'], status=content['status'])
    #     status.create()

    #     return {
    #         "created": True,
    #     }