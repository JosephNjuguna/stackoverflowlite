
class Question():
# constructor of the application
	def __init__(self, Questiondata):
		self.quiz = Questiondata().qdata()
		self.answer = Answersdata().answers()
# posting a single question
	def create_question(self, question):
		questiondata = question
		self.quiz.append(questiondata)
# get all questions
	def get_question(self, args):
		allquestion = self.quiz
		return allquestion
# get a single question
	def get_single_question(self, questionid):
		single_quiz = [q for q in self.quiz if q['question_id'] == questionid]
		if not single_quiz:
			return"Question id not found"
		return single_quiz
# get a single questions with answers
	def get_question_with_answers(self, id):
	    single_quiz = [q for q in self.quiz if q['question_id'] == id]
	    if not single_quiz:
		    return"Question Id doesnot exist or has been deleted"
	    single= single_quiz
	    single_quiz_answer= [q for q in self.answer if q['question_id']== id]
	    if not single_quiz_answer:
		    return "That question has no answers yet. That question id not found in answers"
	    single_answers=  single_quiz_answer
	    full_question = [ single, single_answers]
	    return full_question

#create answer
	def create_answer(self, question):
    		questiondata = question
		self.quiz.append(questiondata)
		
# get a single questions and single answer..(single answer)
	def get_single_answersfor_question(self,id):
	    single_answer = [a for a in self.answer if a['answers_id'] == id]
	    if not single_answer:
		    return "Answers Id doesnot exist or has been deleted"
	    return single_answer   	
# get a single question to update it
	def update_single_question(self, id, updated_question):
		one_question = [q for q in self.quiz if q['id'] == id]
		if not one_question:
		   return "Question Id not found"
		one_question[0]['question'] = updated_question
		return one_question
# get a single question to delete it
	def delete_single_question(self, id):
		single_quiz = [q for q in quiz if n['id'] == int(id)]
		return jsonify({"deleted data": quiz})
		if not single_quiz:
			return "Question id not found"
		quiz.remove(single_quiz[0])

