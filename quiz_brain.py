class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You have completed the quiz.")
            print(f"Your final score is: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} T or F? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

'''from main import question_bank

quiz_on = True

while True:

    correct_count = 0

    for i in range(len(question_bank)):
        question = question_bank[i].text
        answer = question_bank[i].answer

        provided_answer = input(f"{question} T or F? ")
        if provided_answer[0].upper() == answer[0]:
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect!")

    print("This is the end of the quiz.")
    if correct_count == 12:
        print("Excellent Job! You got all 12 correct!")
    else:
        print(f"You got {correct_count} questions correct.")

    replay = input("Try Again? Y or N")
    if replay[0].upper() == "Y":
        correct_count = 0
        game_on = True
    else:
        print("Thanks for playing!")
        break'''
