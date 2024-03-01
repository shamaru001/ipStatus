import sys
from controllers.auth import AuthController
from controllers.ping import PingController
from controllers.status import StatusController
from controllers.user import UserController
from controllers.address import AddressController
from middleware.authorization import token_required


def router(app):
    
    #USERS
    @app.route('/user', methods=['GET'])
    @token_required
    def getAllUsers():
        return UserController.getAll()

    @app.route('/user/<int:id>', methods=['GET'])
    @token_required
    def getOneUser(id): 
        return UserController.get(id)
    
    @app.route('/user', methods=['POST'])
    def createUser():
        return UserController.post()
    
    #LOGIN
    @app.route('/auth', methods=['POST'])
    def login():
        return AuthController.login()

   #PING
    @app.route('/ping/<int:address_id>', methods=['GET'])
    @token_required
    def ping(address_id):
        return PingController.checkAddress(address_id)
    
    #ADDRESSES
    @app.route('/address', methods=['GET'])
    @token_required
    def getAllAddresses():
        return AddressController.getAll()

    @app.route('/address/<int:id>', methods=['GET'])
    @token_required
    def getOneAddress(id): 
        return AddressController.get(id)
    
    @app.route('/address', methods=['POST'])
    def createAddress():
        return AddressController.post()


    #STATUS
    @app.route('/status', methods=['GET'])
    @token_required
    def getAllStatus():
        return StatusController.getAll()

    @app.route('/status/<int:id>', methods=['GET'])
    @token_required
    def getOneStatus(id): 
        return StatusController.get(id)
    
    @app.route('/status', methods=['POST'])
    def createStatus():
        return StatusController.post()

