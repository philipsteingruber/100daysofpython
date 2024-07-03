class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_id = 0
        self.score = 0

    def next_question(self) -> None:
        question = self.questions_list[self.question_id]
        user_answer = input(f"{self.question_id + 1}: {question.text} - (True/False) ")
        self.check_answer(user_answer, question.answer)
        self.question_id += 1

    def still_has_questions(self) -> bool:
        return self.question_id < len(self.questions_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        answer_is_correct = user_answer.casefold() == correct_answer.casefold()
        if answer_is_correct:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        return answer_is_correct
