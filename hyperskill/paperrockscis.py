import random
default_options = ['scissors', 'rock', 'paper']
keywins = {'rock': "fire, scissors, snake, human, tree, wolf, sponge", 'fire': "scissors, snake, human, tree, wolf, sponge, paper", 'scissors': "snake, human, tree, wolf, sponge, paper, air", "snake": "human, tree, wolf, sponge, paper, air, water", "human":"tree, wolf, sponge, paper, air, water, dragon", "tree": " wolf, sponge, paper, air, water, dragon, devil", "wolf": "sponge, paper, air, water, dragon, devil, lightning", "sponge" : "paper, air, water, dragon, devil, lightning, gun", "paper": "air, water, dragon, devil, lightning, gun, rock"}
name = input("Enter your name: ")
print("Hello, "+name)
rating = open('rating.txt', "r")
for line in rating:
    line = line.split()
    if line[0] == name:
        score = int(line[1])
    else:
        score = 0
options = input().split(",")
if len(options) == 1:
    options = default_options
print("Okay, let's start")
while True:
    computer = random.choice(options)
    user_option = input()
    r = keywins.get(user_option)
    l = keywins.get(computer)
    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == '!rating':
        print(f"Your rating: {score}")
    elif user_option not in keywins and user_option != '!exit':
        print("Invalid input")
        continue
    elif computer in r:
        print(f"Well done. Computer chose {computer} and failed")
        score += 100
    elif computer == user_option:
        print(f"There is a draw ({computer})")
        score += 50
    else:
        print(f"Sorry, but computer chose {computer}")
