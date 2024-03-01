import platform
import subprocess
import sys
from flask import request
from models.address import addressModel
from models.status import statusModel

class PingController():

    @staticmethod 
    def doPing(host):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0
    
    @classmethod
    def checkAddress(self, address_id):
        address = addressModel.findOne(addressModel.id, address_id)
        status = self.doPing(address.address)

        new_status = statusModel(address_id=address_id, status=status)
        new_status.create()

        return {
            "status": status
        }
