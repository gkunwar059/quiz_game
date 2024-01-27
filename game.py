print("Welcome to my computer quiz !")

playing=input("Do you want to play ? ")
# print(playing)


if playing.lower() !="yes": 

    quit()

print("Lets play the Game ")
score=0

answer=input("What is the Full Form of CPU ?").lower()
if answer=="central processing unit":
    print("Congratulations ! You are Correct.")
    score+=1

    # score=score+1
else:
    print("Try Again !!")
    # score-=1

answer=input("What is the Full Form of RAM ?").lower()
if answer=="random acess memory":
    print("Congratulations ! You are Correct.")
    score+=1
else:
    print("Try Again !!")
    # score-=1


answer=input("What is the Full Form of ROM ?").lower()
if answer=="read only memory":
    print("Congratulations ! You are Correct.")
    score+=1
else:
    print("Try Again !!")
    # score-=1


answer=input("What is the Full Form of GPU ?").lower()
if answer=="graphic processing unit":
    print("Congratulations ! You are Correct.")
    score+=1
else:
    print("Try Again !!")
    # score-=1


print("You have got  " + str(score) +"  Correct Answer !")
print("You have got  " + str((score/4)*100) +"%")