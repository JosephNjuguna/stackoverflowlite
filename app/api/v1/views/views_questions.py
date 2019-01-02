@question_api.route('/getquestions', methods= ['GET'])
def get_all_question():
	allquestions = quiz.get_question(args)
	if allquestions =='':
		return "no Data found"
	return make_response(jsonify({"data": allquestions}),200)
