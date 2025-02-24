import random

keep_going = 'yes'
#intro
print("Welcome to Lucky Unicorn!")

#asks how much money the player wants to use
startbalance = int(input("How much money would you like to play with? "))

#if the number inputed is less than 1 or bigger than 10 it will tell the user to use a number between 1 and 10
while startbalance < 1 or startbalance > 10:
    print("Sorry, you need to play with at least one dollar no more than ten dollars.")
    startbalance = int(input("How much money would you like to play with? "))

#prints the number the user entered if it is valid
else:
    print(f"You have input ${startbalance}")

#makes balance the start balance with the ability to change
balance = startbalance

while keep_going == 'yes':
    
    #asks how much the user wants to bet and tells them no if the bet is to high, also reaskes question
    bet = int(input("How much would you like to bet? "))
    while bet > balance:
        print("Sorry, you dont have enough money.")
        bet = int(input("How much would you like to bet? "))

    #says how much it is betting with
    else:
        print(f"Betting with ${bet}")

    #asks to type spin to bet and makes it lowercase
    input(f"Press Enter to bet ${bet} ")
   
    #chooses random number for animal
    
    animal = random.randint(1, 100)

    #changes balance and prints it if unicorn is drawn
    if animal == 100:
        print("Unicorn! Congratulations you hit the jackpot!")
        int(bet) * int(5)
        addition = int(balance) + int(bet)
        print(f"Your balance is now ${addition}")
    #changes balance and prints it if horse is drawn
    elif animal <= 33:
        print("Horse! Better luck lext time.")
        int(bet) - int(2)
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")
    #changes balance and prints it if zebra is drawn
    elif animal <= 66:
        print("Zebra! Better luck lext time.")
        int(bet) - int(2)
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")
    #changes balance and prints it if donkey is drawn
    else: 
        animal <= 99
        print("DONKEY! YOU LOSE!")
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")
    
    if balance == 0:
        keep_going = 'no'
    else:
    #asks the user if they want to continue
        keepgoing = input("Would you like to continue? ")
    keep_going = keepgoing.lower()
    if keep_going == 'yes':
        print("lets continue.")
    else:
        print("Sad to see you go.")