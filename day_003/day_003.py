# Choose your own adventure game.

print('''
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|
''')

print("Welcome to Dino Danger.")

option1 = input("You hear a branch snap in the bush to your left, what do you do? (1) Run, or (2) Stand you Ground.")

if option1 == "2":
    print("The dinosaur eats you whole you die.")

elif option1 == "1":
    option2 = input("You start running but you hear the dinosaur approching quickly from behind, what do you do? (1) Turn left or (2) Turn Right.")

    if option2 == "2":
        print("You trip over a branch and the dinosaur eats you whole, you die.")

    elif option2 == "1":
        print("You find a spear and kill the dinosaur, you survive.")

else:
    print("You did not select a valid option game aborted.")