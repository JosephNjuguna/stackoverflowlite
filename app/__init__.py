from flask import Flask

# local import
from instance.config import app_config

create_app = Flask(__name__)
create_app.config['SECRET_KEY'] = 'alkdsuhjvksudjvnksnbkj'

from app.api.v1.views.views_questions import question_api as question_blueprint
from app.api.v1.views.views_users import user_api as user_blueprint
from app.api.v2 import version_two as userv2_blueprint
from app.api.v3 import version_three as userv3_blueprint
from app.api.v3 import models

create_app.register_blueprint(question_blueprint,url_prefix='/api/v1')
create_app.register_blueprint(user_blueprint,url_prefix='/api/v1')
create_app.register_blueprint(userv2_blueprint,url_prefix='/api/v2')
create_app.register_blueprint(userv3_blueprint,url_prefix = '/api/v3')

