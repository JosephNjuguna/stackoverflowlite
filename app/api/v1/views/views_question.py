#get_single_answersfor_question
@question_api.route('/getquestion/<string:quiz_id>/answers/<string:answer_id>', methods=['GET'])
def get_one_answer(quiz_id):	
	id_data = quiz_id
	single_question = quiz.get_single_answersfor_question(id_data)
	return make_response (jsonify({"updated data": single_question}), 200)
