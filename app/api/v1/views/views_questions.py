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
