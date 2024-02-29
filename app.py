from flask import Flask
from controllers.user import UserController

#Setup server
app = Flask(__name__)
app.add_url_rule('/user', view_func=UserController.as_view('user'))


# if __name__  == '__main__':
#     app.run(port=4000)