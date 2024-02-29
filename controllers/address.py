from flask.views import MethodView

from models.address import addressModel


class UserController(MethodView):

    def get(self):
        return 'hola desde un metodo'
    
    def post(self):
        return 'post'
    
    def delete(self):
        return 'delete'
    
    def patch(self): 
        return 'patch'
    
    def put(self):
        return 'put'