from flask import Flask, request, jsonify, make_response, Blueprint
from app.api.v1.models.models import Question
from app.api.data.questionsdata import Questiondata
from app.api.data.userdata import Usersdata

from app.api.authorization.auth import token_required

import uuid
import datetime

question_api = Blueprint('question_api', __name__)
quiz = Question(Questiondata)
args = ""

@question_api.route('/getquestion/<string:quiz_id>',methods=['GET'])
def get_one_question(quiz_id):	
	id_data = quiz_id
	single_question = quiz.get_single_question(id_data)
	return make_response (jsonify({"updated data": single_question}), 200)
