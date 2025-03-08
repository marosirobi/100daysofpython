class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.q_num

    def check_answer(self, user_answer,correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:

            print("Sorry, that's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.q_num+1}\n")
        self.q_num += 1
    def next_question(self):
        current_q = self.question_list[self.q_num]
        user_answer = input(f"Q.{self.q_num+1}: {current_q.question} (True/False) ")
        self.check_answer(user_answer,current_q.answer)


