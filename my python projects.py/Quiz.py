quiz = {
    "question 1":{
        "question":"what is the capital of south africa".
        "answer" : "Cape Town,Pretoria,Bloemfointen"
    },
    "question 2":{
        "question": "what is the capital of Botswana".
        "answer" : "gaborone"
    },
    "question 3":{
        "question": "what is the capital of zimbabwe".
        "answer": "Harare"
    },
    "question 4":{
        "question": "what is the capital of Malawi".
        "answer": "Lilongwe"
    },
    "question 5":{
        "question": "what is the capital of swaziland".
        "answer" : "Mbabane"
    },
    "question 6":{
        "question":"what is the capital of Egypt"
        "answer": "cairo"
    },
    "question 7":{
        "question":"what is the capital of lesotho"
        "answer":"Maseru"
    }
       }.

score = 0

for key ,value in quiz.items():
    print (value ['question'])
    answer= input("Answer?")

if answer.lower() == value ['answer'].lower():
    print('correct')
    score = score +1
    print ("Your score is:"+ str(score))

else:
    print("wrong")
    print("The answer is:" + value['answer'])
    print("Your score is:"+ str(score))
    print("")
    print("")


    print("you got " + str(score)+ "out of 7 questions correctly")
    print("your percentage is" + str(int(score/7 +100 +"%")))
    


