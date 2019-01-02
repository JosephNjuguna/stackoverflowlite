
from app.api.data.questionsdata import Questiondata
from app.api.data import userdata
from app.api.data.ansersdata import Answersdata
from werkzeug.security import check_password_hash
from flask import Flask
import uuid
import jwt
import datetime

from instance.config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

userlist = userdata.Usersdata()

name_error = 'Username not found'
password_error = 'Invalid Password'




