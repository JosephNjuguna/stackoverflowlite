
@question_api.route('/getquestion/<string:quiz_id>/answers/postanswer/', methods= ['POST'])
@token_required
def reply_question(current_user, q_id):
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
		"answer": questiondata['answer'],
		"category": questiondata['category'],
		"datetime": datetime.datetime.utcnow(),
		"answer_id": question_id,
		"author_id":a_id
	}
	answerposted = quiz.post_answer(question)
	return make_response(jsonify({"answer posted": answerposted}),200)

