import art
import random
def standplay():
    global cputotal, cpucards, usertotal, usercards, continueplay
    while cputotal < 17:
        cpucards.append(random.choice(cards))
        cputotal = sum(cpucards)
    if usertotal > 21:
        print("BUST your total went over 21")
    if cputotal > usertotal and cputotal <= 21:
        print(f"your total was {usertotal} and computers total was {cputotal} computer wins")
    if usertotal > cputotal:
        print(f"your total was {usertotal} and computers total was {cputotal} you win")
    if usertotal == cputotal:
        print(f"your total was {usertotal} and computers total was {cputotal} it's a draw")
    if cputotal > 21:
        print(f"your total was {usertotal} and computers total was {cputotal} computer went over 21 you win")
    continueplay=False
def hitplay():
    global continueplay, usertotal
    usercards.append(random.choice(cards))
    usertotal = sum(usercards)
    if usertotal > 21:
        print("BUST your total went over 21")
        continueplay=False
def check_for_ace_converting():
    global usercards, usertotal
    while usertotal > 21 and 11 in usercards:
        usercards[usercards.index(11)] = 1
        usertotal = sum(usercards)
play=input("do you want to play a game of blackjack type: y for yes or type: n for no : ").lower()
if play=="y":
    continueplay= True
if play=="n":
    continueplay= False
usertotal=0
cputotal=0
gameover=False
while continueplay == True:
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    usercards=random.sample(cards, 2)
    cpucards=random.sample(cards, 2)
    usertotal=sum(usercards)
    cputotal=sum(cpucards)
    while continueplay == True:
        firstchoice=input(f"Your hand is {usercards} ur total is {usertotal} the computers hand is [{cpucards[0]}, Hidden] do you want to hit or stand? for hit type: N or for stand type: Y \n").strip().lower()
        if firstchoice=="n":
            check_for_ace_converting()
            hitplay()
        if firstchoice=="y" :
            check_for_ace_converting()
            standplay()
            continueplay=False
    shouldcontinue = input(f"type y to play another game or n for no: ").strip().lower()
    if shouldcontinue == "y":
        continueplay = True
    if shouldcontinue == "n":
        continueplay = False