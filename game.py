import json
import random


with open('questions.json', 'r') as f:
  data = json.load(f)


class Game():

    def get_question_answers(level):
        level_string = str(level)
        random_choice = random.choice(data[level_string])
        question = random_choice['question']
        A_ans = random_choice['A']
        B_ans = random_choice['B']
        C_ans = random_choice['C']
        D_ans = random_choice['D']
        correct_answer = random_choice['correct']
        return question, A_ans, B_ans, C_ans, D_ans, correct_answer

    