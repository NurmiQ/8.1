import random
from QA import Question

dict = {
    "How many days do we have in a week?": {
        "answers": ["seven", "7"],
        "difficulty": 1,
        "author": "Michael Jordan",
        "theme": "General questions"
    },
    "How many days are there in a normal year?": {
        "answers": ["365"],
        "difficulty": 3,
        "author": "Lebron James",
        "theme": "General questions"
    },
    "How many colors are there in a rainbow?": {
        "answers": ["seven", "7"],
        "difficulty": 3,
        "author": "Dwane Wade",
        "theme": "Nature"
    },
    "Which animal is known as the ‘Ship of the Desert?": {
        "answers": ["camel"],
        "difficulty": 4,
        "author": "Stephen Curry",
        "theme": "Animals"
    },
    "How many letters are there in the English alphabet?": {
        "answers": ["26"],
        "difficulty": 4,
        "author": "Klay Thompson",
        "theme": "Language"
    },
    "How many consonants are there in the English alphabet?": {
        "answers": ["21"],
        "difficulty": 5,
        "author": "Kevin Durant",
        "theme": "Language"
    },
    "How many sides are there in a triangle?": {
        "answers": ["3", "three"],
        "difficulty": 1,
        "author": "Ray Allen",
        "theme": "Math"
    },
    "Which month of the year has the least number of days?": {
        "answers": ["february"],
        "difficulty": 2,
        "author": "Leo Messi",
        "theme": "General questions"
    },
    "Which are the vowels in the English alphabet series?": {
        "answers": ["a, e, i, o, u"],
        "difficulty": 5,
        "author": "Mo Salah",
        "theme": "Language"
    },
    "Which animal is called King of Jungle?": {
        "answers": ["lion"],
        "difficulty": 1,
        "author": "Sadio Mane",
        "theme": "Animals"
    },
}


def read_dict(dict):
    questions_list = []
    for key in dict.keys():
        questions_list.append(Question(
            text=key,
            author=dict[key]["author"],
            difficulty=dict[key]["difficulty"],
            answers=dict[key]["answers"],
            theme=dict[key]["theme"]
        ))

    return questions_list


questions = read_dict(dict)
random.shuffle(questions)

for question in questions:
    print(
        f'Question {questions.index(question) + 1}, theme: {question.theme}, difficulty: {question.difficulty}/5, author: {question.author}')
    print(question)

    user_answer = input('Write the answer ')

    if user_answer == 'stop':
        break

    question.user_answer = user_answer
    question.is_asked = True

    if question.is_correct():
        print(f'Answer is right, you got {question.score} points')
        print()
    else:
        print(f"Answer is not right. Right answer - {' or '.join(question.answers)}")
        question.is_right = False
        print()


def statistics(questions_list):
    stats = {
        'total_questions': 0,
        'right_answers': 0,
        'total_score': 0
    }

    for question in questions_list:
        if question.is_asked:
            stats['total_questions'] += 1
            if question.is_right:
                stats['right_answers'] += 1
                stats['total_score'] += question.score

    return stats


stats = statistics(questions)

print(f"""That's all!
You answered {stats['right_answers']} out of {stats['total_questions']} and you got {stats['total_score']} points""")
