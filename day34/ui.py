import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 14))
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text((150, 125), text='Some Question Text', fill=THEME_COLOR, font=('Arial', 14, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file='./images/true.png')
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file='./images/false.png')
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            self.true_button.config(state='active')
            self.false_button.config(state='active')
            self.score_label.config(text=f'Score: {self.quiz_brain.score}')
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text='End of the quiz.')

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer('true')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
        self.window.after(ms=1000, func=self.get_next_question)
