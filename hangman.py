import time
import random
import turtle
myTurtle = turtle.Turtle()
name = input( "what is your name?  ")

print("hello, ",name)

time.sleep(2)

print("let's begin")

secrets=["dog","fish","turtle","cat","spark","zoe","jacob"]

index = random.randint(0,7)

word = secrets[index]

turns = 7

guess =""

for currentTurn in range(1,10):

    failed=0
    for letter in word:
        if letter in guess:
            print(letter)
        else:
            print("_")
            failed=failed+1
    if failed==0:
        print("you won " "the word was ",word)
        break
    print("")

    character= input("guess a letter ")
    print("")
    guess=guess+character
    if character not in word:
        print("wrong")
      
        print("you have ",turns," turns left.")
        if turns == 7:

            # move turtle to starting position-25.64,-39.81-25.64,-39.81
            
            myTurtle.penup()
            myTurtle.setposition(100, -100)
            myTurtle.pendown()
            turns = turns- 1

            #hangman's pole
            myTurtle.left(90)
            myTurtle.forward(200)
            
        elif turns == 6:
            #hangman's head
            myTurtle.left(90)
            myTurtle.forward(130)
            myTurtle.circle(20)
            turns = turns- 1

        elif turns == 5:
            #hangman's body
            myTurtle.penup()
            myTurtle.setposition(-30.00,100.00)
            myTurtle.left(90)
            myTurtle.forward(40)
            myTurtle.pendown()
            myTurtle.forward(120)
            turns = turns- 1

        elif turns == 4:
            #hangman's left arm
            myTurtle.setposition(-30.00,10.00)
            myTurtle.right(150)
            myTurtle.forward(70)
            turns = turns- 1

        elif turns == 3:
            #hangman's right arm
            myTurtle.penup()
            myTurtle.setposition(-30.00,10.00)
            myTurtle.right(80)
            myTurtle.pendown()
            myTurtle.forward(70)
            turns = turns- 1
        elif turns == 2:
            #hangman's right leg
            myTurtle.right(130)
            myTurtle.penup()
            myTurtle.setposition(-30.00,10.00)
            myTurtle.forward(50)
            myTurtle.left(20)
            myTurtle.pendown()
            myTurtle.forward(70)
            turns = turns- 1
        elif turns == 1:
            #hangman's left leg
            myTurtle.penup()
            myTurtle.setposition(-25.64,-39.81)
            myTurtle.right(40)
            myTurtle.pendown()
            myTurtle.forward(70)
            
            # move turtle to starting position-25.64,-39.81-25.64,-39.81
            myTurtle = turtle.Turtle()
            myTurtle.penup()
            myTurtle.setposition(100, -100)
            myTurtle.pendown()
            turns = turns- 1
        else:
            print("you lose.")
            

#if failed > 0:
   # print("you lose.")

