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
@question_api.route('/getquestions', methods= ['GET'])
def get_all_question():
	allquestions = quiz.get_question(args)
	if allquestions =='':
		return "no Data found"
	return make_response(jsonify({"data": allquestions}),200)
@question_api.route('/postquestion/<string:q_id>', methods= ['POST'])
def add_one_question(current_user, q_id):
	userid = str(q_id)
	questiondata = request.get_json()
	users =  Usersdata().authdata()
	confirm_id = [uid for uid in users if uid['public_id']== userid]
	if not confirm_id:
	    return"User id not found"
	if questiondata == {}:
		return "Empty json fields"
	question_id = str(uuid.uuid4())
	question ={ 
		"author" :  questiondata['author'],
		"question": questiondata['question'],
		"category": questiondata['category'],
		"datetime": datetime.datetime.utcnow(),
		"question_id": question_id,
		"author_id":a_id
	}
	questionposted = quiz.create_question(question)
	allquestions = quiz.get_question(args)
	if allquestions =='':
		return "no Data found"
	return make_response(jsonify({"question posted": allquestions}),200)
