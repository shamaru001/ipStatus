import sys
from controllers.auth import AuthController
from controllers.user import UserController
from middleware.authorization import token_required


def router(app):
    
    #USERS
    @app.route('/user', methods=['GET'])
    @token_required
    def getAllUsers():
        return UserController.getAll()

    @app.route('/user/<int:id>', methods=['GET'])
    def getOneUser(id): 
        return UserController.get(id)
    
    @app.route('/user', methods=['POST'])
    def createUser():
        return UserController.post()
    
    @app.route('/auth', methods=['POST'])
    def login():
        return AuthController.login()



