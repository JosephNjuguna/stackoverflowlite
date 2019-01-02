#get one question with all the answers that it will have
@question_api.route('/getquestion/<string:quiz_id>/answers', methods=['GET'])
def get_question_with_answers_route(quiz_id):
	questionanswers = quiz.get_question_with_answers(quiz_id)
	return make_response(jsonify({"question with answers": questionanswers}))
