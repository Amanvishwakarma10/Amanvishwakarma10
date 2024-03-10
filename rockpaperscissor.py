import random
elements = ['rock','paper','scissor']
computer = random.choice(elements)
user = input("ITS YOUR TURN :")
print("computers turn:",computer)

if user == computer :
    print("its a tie!")
    print("startt again")
elif(user == 'rock' and computer == 'scissors') or \
    (user == 'scissors' and computer == 'paper') or \
    (user == 'paper' and computer == 'rock'):
    print("You win!")
else:
    print("you Lose!")
    print("thanks for playing")