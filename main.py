import random

user_wins = 0
computer_wins = 0
choices = ['rock', 'paper', 'scissors']


while True:
    user_pick = input("Pick either rock, paper, or scissors. Type Q to quit: ").lower()
    if user_pick == 'q':
        break
    if user_pick not in choices:
        continue
    random_num = random.randint(0,2)
    # rock is 0, paper is 1, and scissors is 2
    computer_pick = choices[random_num]
    print("computer picked ",computer_pick)

    if user_pick == 'rock' and computer_pick == 'scissors':
        print("You win!")
        user_wins += 1
    elif user_pick == 'paper' and computer_pick == 'rock':
        print("You win!")
        user_wins += 1
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print("You win!")
        user_wins += 1
    else:
        print("You lost, Computer wins")
        computer_wins+=1

print("you won ",user_wins, "times.")
print("the computer won ",computer_wins, "times.")
print("Goodbye")





