from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mail import Mail

from database.db import initialize_db
from resources.errors import errors


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)

from resources.routes import initialize_routes

v1 = Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://dbsuser:dbpassword@cluster0.4jbmt.mongodb.net/elektromaid?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(v1)
@app.route("/") 
def home_view(): 
        return "<center><h1>Welcome to Elektromaid Api server</h1></center>"

