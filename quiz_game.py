corr = 0
incorr = 0
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let´s play :). I'm going to make you six questions. Your qualification is going to be based on the questions you answer right.")

answer = input("What does CPU stand for? \n please type in minus \n")

if answer == "central processing unit":
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

answer = input("What does RAM stand for? \n please type in minus \n")

if answer == "random access memory":
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

answer = input("What does ROM stand for? \n please type in minus \n")

if answer == "read only memory":
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

answer = input("The memories are made up of a certain number of cells. Each of them is identified by a number called: Select an answer. Option 1: Memory capactity, Option 2: Data register, Option 3: Counter register, Option 4: Memory adress \n please type in minus \n")

option1 = "memory capacity"

option2 = "data register"

option3 = "counter register"

option4 = "memory adress"


if answer == option4:
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

answer = input("What does SSD stand for? \n please type in minus \n")
if answer == "solid state unit":
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

answer = input("What does HDD stand for? \n please type in minus \n")
if answer == "hard drive disk":
    print('Correct! ')
    corr = corr + 1
else:
    print('Incorrect :(')
    incorr = incorr + 1

if corr >= 4:
    print('Congratulations, you passed the exam!')
else:
    print('Unlucky, you didnt pass the exam!')

print("you had ",corr," correct points, and ",incorr," incorrect points")