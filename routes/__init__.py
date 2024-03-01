from controllers.user import UserController


def router(app):
    
    #USERS
    @app.route('/user', methods=['GET'])
    def getAllUsers():
        return UserController.getAll()

    @app.route('/user/<int:id>', methods=['GET'])
    def getOneUser(id): 
        return UserController.get(id)
    
    @app.route('/user', methods=['POST'])
    def createUser(): 
        return UserController.post()



