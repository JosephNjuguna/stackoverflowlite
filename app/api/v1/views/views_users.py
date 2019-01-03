from flask import Flask, request, jsonify, make_response, Blueprint
from app.api.v1.models.models import  Users
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import uuid
import jwt
import datetime

from instance.config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from app.api.data.userdata import Usersdata
from app.api.authorization.auth import token_required

user_api =  Blueprint('users_api',__name__)
userauthdata = Users()
userdata = Usersdata().authdata()

args = ""
alert_error = "Either Email or Password dont match "
empty = "Empty json.Cant be empty"

"""user sign in """
@user_api.route('/auth/signup', methods= ['POST'])
def sign_up_user():
    data = request.get_json()
    if data == {}:
        return make_response("Fields can`t be empty"),401
    for infoauth in data.items():
        if data['name'] == '':
            return make_response("Empty Name"),401
        if data['email'] == '':
            return make_response("Empty Email"),401
        if data['password'] == '':
            return make_response("Empty Password"),401
    public_id = str(uuid.uuid4())
    hashed_password = generate_password_hash(data['password'], method= 'sha256')
    signupinfo = {
        "name":data['name'],
        "id": public_id,
        "email": data['email'],
        "password" : hashed_password,
        "date" : datetime.datetime.utcnow()
    }
    newuser = userauthdata.create_a_new_user(signupinfo)
    return make_response(jsonify({"message":newuser}),201)
