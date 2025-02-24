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

    #amount of each animal 
    unicorn = 0
    horse = 0
    zebra = 0
    donkey = 0

    #asks to type spin to bet and makes it lowercase
    spin = input(f"Type spin to bet ${bet} ")
    spin_1 = spin.lower

    #choosesn random number for chance of animal
    import random
    animal = random.randint(1, 100)

    #chances for animal to happen and what happens to balance
    if animal == 100:
        print("Unicorn! Congratulations you hit the jackpot!")
        int(bet) * int(5)
        addition = int(balance) + int(bet)
        print(f"Your balance is now ${addition}")
    elif animal >= 99:
        print("Horse! Better luck lext time.")
        int(bet) - int(2)
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")
    elif animal >= 66:
        print("Zebra! Better luck lext time.")
        int(bet) - int(2)
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")
    elif animal >= 33:
        print("DONKEY! YOU LOSE!")
        subtract = int(balance) - int(bet)
        print(f"Your balance is now ${subtract}")

    #asks the user if they want to continue
    keepgoing = input("Would you like to continue? ")
    keep_going = keepgoing.lower()
    if keep_going == 'yes':
        print("lets continue.")
    else:
        print("Sad to see you go.")