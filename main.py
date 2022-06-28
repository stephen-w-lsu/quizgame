from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_answer = q["answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

