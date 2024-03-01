from flask import Flask
from routes import router

#Setup server
app = Flask(__name__)

router(app)
# if __name__  == '__main__':
#     app.run(port=4000)