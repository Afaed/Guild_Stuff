import json
#settings
questions_key = []
answers_key = []
incorrect_key = []
#initalization
score = 0
player_answers = []

with open ("data.json") as file:
    
    dictionary = json.load(file).get("results")
    
    for sub_dict in dictionary:
        question = sub_dict.get("question")
        answer = sub_dict.get("correct_answer")
        incorrect = sub_dict.get("incorrect_answers")
        
        questions_key.append(question)
        answers_key.append(answer)
        incorrect_key.append(incorrect)
