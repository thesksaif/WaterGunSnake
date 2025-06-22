# 🕹️ Rules of the Game:
# Each player chooses one of the three options:

# 🐍 Snake = 1

# 💧 Water = -1

# 🔫 Gun.  = 0

# | Choice 1 | Choice 2 | Winner | Reason                 |
# | -------- | -------- | ------ | ---------------------- |
# | Snake    | Water    | Snake  | Snake drinks the water |
# | Water    | Gun      | Water  | Water drowns the gun   |
# | Gun      | Snake    | Gun    | Gun kills the snake    |
# | Same     | Same     | Draw   | No winner              |

import random;

computer = random.choice([-1, 0, 1])
yourstr = input("Enter a choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[yourstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its Draw")
else:
    if(computer == -1 and you == 0):
        print("Water drowns the gun, You win")
    elif(computer == 1 and you == -1):
        print("Snake drinks the water, You loss")
    elif(computer == 0 and you == 1):
        print("Gun kills the snake, You win")
