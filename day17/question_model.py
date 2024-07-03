class Question:
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f"{self.text} - {self.answer}"
