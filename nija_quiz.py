nija = {
    1: {
        'question': 'What is the capital city of Nigeria?',
        'answer': 'Abuja'
    },
    2: {
        'question': 'Which river is the longest in Nigeria?',
        'answer': 'Niger'
    },
    3: {
        'question': 'What is the largest city in Nigeria by population?',
        'answer': 'Lagos'
    },
    4: {
        'question': 'What is the official language of Nigeria?',
        'answer': 'English'
    },
    5: {
        'question': 'Which ethnic group is the largest in Nigeria?',
        'answer': 'Hausa-Fulani'
    },
    6: {
        'question': 'In what year did Nigeria gain independence?',
        'answer': '1960'
    },
    7: {
        'question': 'What is the currency of Nigeria?',
        'answer': 'Naira'
    },
    8: {
        'question': 'Who is the current President of Nigeria?',
        'answer': 'Bola Ahmed Tinubu'
    },
    9: {
        'question': 'Which Nigerian musician is known as the "African Giant"?',
        'answer': 'Burna Boy'
    },
    10: {
        'question': 'What is the highest mountain in Nigeria?',
        'answer': 'Chappal Waddi'
    },
    11: {
        'question': 'Which Nigerian city is known as the "Centre of Excellence"?',
        'answer': 'Lagos'
    },
    12: {
        'question': 'What is the nickname for the Nigerian national football team?',
        'answer': 'Super Eagles'
    },
    13: {
        'question': 'Which famous Nigerian author wrote "Things Fall Apart"?',
        'answer': 'Chinua Achebe'
    },
    14: {
        'question': 'What is the primary export oil grade of Nigeria?',
        'answer': 'Bonny Light'
    },
    15: {
        'question': 'Which UNESCO World Heritage Site is located in Nigeria?',
        'answer': 'Sukur Cultural Landscape'
    },
    16: {
        'question': 'What is the meaning of the Nigerian national motto "Unity and Faith, Peace and Progress"?',
        'answer': 'To promote unity, faith, peace, and progress in Nigeria'
    },
    17: {
        'question': 'Which Nigerian dish is made with cassava flakes and hot water?',
        'answer': 'Garri'
    },
    18: {
        'question': 'Who is the first woman to become the Finance Minister of Nigeria?',
        'answer': 'Ngozi Okonjo-Iweala'
    },
    19: {
        'question': 'Which Nigerian city is known for its ancient walls and gates?',
        'answer': 'Kano'
    },
    20: {
        'question': 'What is the population of Nigeria (approximately)?',
        'answer': 'Over 200 million'
    },
    21: {
        'question': 'Which river forms a natural boundary between Nigeria and Cameroon?',
        'answer': 'Cross River'
    },
    22: {
        'question': 'In what year did Nigeria become a republic?',
        'answer': '1963'
    },
    23: {
        'question': 'Who is the founder of the Afrobeat music genre?',
        'answer': 'Fela Kuti'
    },
    24: {
        'question': 'What is the traditional clothing for men in Nigeria?',
        'answer': 'Agbada'
    },
    25: {
        'question': 'Which Nigerian city is famous for its ancient bronze artifacts?',
        'answer': 'Benin City'
    },
    26: {
        'question': 'What is the name of the Nigerian national flag?',
        'answer': 'Green-White-Green'
    },
    27: {
        'question': 'Which Nigerian state is known as the "Gateway State"?',
        'answer': 'Ogun State'
    },
    28: {
        'question': 'What is the most widely spoken language in Nigeria?',
        'answer': 'Hausa'
    },
    29: {
        'question': 'Which Nigerian city is known as the "Coal City"?',
        'answer': 'Enugu'
    },
    30: {
        'question': 'What is the name of the famous plateau in Nigeria?',
        'answer': 'Jos Plateau'
    },
}

score = 0

for key, value in nija.items():
    
    print(value['question'])
    answer = input("Input your answer: ")
    print("")
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print("Your Score is " + str(score))
        print("")
    else:
        print("Wrong")
        print("The answer is" + str(value['answer']))
        print("Your Score is " + str(score))
        print("")
        
print("Your total score is " + str(score) + " and your percentage score is " + str(score/30 * 100) + "%")