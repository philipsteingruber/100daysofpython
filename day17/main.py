from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main():
    questions = []
    for question in question_data:
        questions.append(Question(question["text"], question["answer"]))

    quiz = QuizBrain(questions)

    while quiz.still_has_questions():
        quiz.next_question()

    print("Quiz complete!")
    print(f"Your score was {quiz.score} out of {len(quiz.questions_list)}")


if __name__ == "__main__":
    main()
