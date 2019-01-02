#update single question
@question_api.route('/questions/<string:quiz_id>',methods=['PUT'])
@token_required
def update_one_question(current_user,quiz_id):
	data = request.get_json()
	if data == {}:
		return "Empty JSON"
	updated_question = data['question']
	update_q = quiz.update_single_question(quiz_id, updated_question)
	return make_response(jsonify({"updated data":singlequiz[0]}))	
