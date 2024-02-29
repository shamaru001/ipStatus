from flask.views import MethodView
from sqlalchemy import select
from models.user import UserModel
from db import getDB


class UserController(MethodView):

    def get(self):
        with getDB() as conn:
            users = conn.scalars(select(UserModel)).fetchall()
            return users
    
    def post(self):

        user = UserModel(name='123', password='231')
        with getDB() as conn:
            conn
    
    def delete(self):
        return 'delete'
    
    def patch(self): 
        return 'patch'
    
    def put(self):
        return 'put'