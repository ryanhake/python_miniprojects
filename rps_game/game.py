import random

print("*** Rock Paper Scissors ***")

win = 0
loss = 0
tie = 0


while True:
    print(f"Win: {win} Loss: {loss} Tie: {tie}")
    print("""Enter your move:
            r - Rock
            p - Paper
            s - Scissors""")
    Usermove = input("Type one of r, s, or p: ")
    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computermove = 'r'
        print("Rock")
    elif randomnumber == 2:
        computermove = 'p'
        print("Paper")
    elif randomnumber == 3:
        computermove = 's'
        print("Scissors")
    if Usermove == computermove:
        print("It is a tie!")
        tie += 1
    elif Usermove == 'r' and computermove == 's':
        win += 1
        print("You win!")
    elif Usermove == 'p' and computermove == 'r':
        win += 1
        print("You win!")
    elif Usermove == 's' and computermove == 'p':
        win += 1
        print("You win!")
    elif Usermove == 'r' and computermove == 'p':
        loss += 1
        print("You lose :(")
    elif Usermove == 'p' and computermove == 's':
        loss += 1
        print("You lose :(")
    elif Usermove == 's' and computermove == 'r':
        loss += 1
        print("You lose :(")

