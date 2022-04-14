class GenericQuestion:
    def __init__(self, text, author, difficulty, answers, theme, is_asked=False, is_right=True, user_answer=""):
        self.text = text
        self.author = author
        self.difficulty = difficulty
        self.answers = answers
        self.theme = theme
        self.user_answer = user_answer
        self.is_asked = is_asked
        self.is_right = is_right
        self.score = difficulty * 10

    def __repr__(self):
        return self.text

class Question(GenericQuestion):

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer in self.answers

    def build_question(self):
        return f"Theme: {self.theme}, difficulty: {self.difficulty} \n{self.text}"

