#delete single question
@question_api.route('/questions/<string:quiz_id>',methods=['DELETE'])
@token_required
def delete_one_question(current_user, quiz_id):
	single_question = quiz.delete_single_question(quiz_id)
	return make_response(jsonify({"deleted" : single_question}))
