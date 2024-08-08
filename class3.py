a="Welcome to Computer Quiz"
print(a.center(80))
x=input("Do you want to play the game?\n")
if():
    x.lower!= "yes"
    print("Sad to see you go!")
else:
    print("Let's start the game!")
print("There are five questions and each question carries one point\n(Alert: Write only one answer)")
score=0

question_1=input("Question number 1:\nWhat is the full form of ROM?\n")
if(question_1.lower()=="read only memory"):
    print("Correct")
    score=score+1
    print("Your score is", score)
else:
    print("Incorrect")

question_2=input("Question number 2:\nWhich device is required for the Internet connection?\n")
if(question_2.lower()=="modem"):
    print("Correct")
    score=score+1
    print("Your score is", score)
else:
    print("Incorrect")

question_3=input("Question number 3:\nWhat is meant by ASCII?\n")
if(question_3.lower()==" american standard code for information interchange"):
    print("Correct")
    score=score+1
    print("Your score is", score)
else:
    print("Incorrect")

question_4=input("Question number 4:\nA computer program that converts an entire program into machine language is called?\n")
if(question_4.lower()=="compiler"):
    print("Correct")
    score=score+1
    print("Your score is", score)
else:
    print("Incorrect")

question_5=input("Question number 5:\nWhich of the following is also known as brain of computer?\n")
if(question_5.lower()=="cpu"):
    print("Correct")
    score=score+1
    print("Your score is", score)
elif(question_5.lower()=="central processing system"):
    print("Correct")
    score=score+1
    print("Your score is", score)
else:
    print("Incorrect")
    
if(score>=3):
    print("Congratulation! You have scored", score ,"points")
else:
    print("You've only scored", score ,"points :)")

print("you have got", (score/5)*100, "\% answers correct!")