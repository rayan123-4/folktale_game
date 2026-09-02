print("The Great Raccoon Bakery Heist")
print("You are a hungry Raccoon standing in the dark alley behind a bakery in the middle of the night. You smell fresh croissants.")

newFriends = False
madeFriends = False

friend1 = ""
friend2 = ""

isHungry = True
while isHungry:
    print("Choose an option:")
    print("a: Climb through the open window, however the guard is sleeping right next to it.")
    print("b: Sneak through the back door, but the alarm system is active.")
    print("c: Walk through the front door like a regular customer.")
    choice = input("Enter your choice (a, b, or c): ").lower()
    if choice == "c":
        print("Simple is the way to go. You grab a croissant and walk out, like no one ever suspected a thing.")
        isHungry = False
    elif choice == "a":
        print("You climb smoothly through the window and the guard is still asleep, however you knock over the tray of crossaints and the guard wakes up and chases you down.")
        isHungry = False
    elif choice == "b":
        print("You sneak through the back door and manage to avoid the alarms and the guard, but you took too long and all the crossaints are gone and there's only a mere slice of bread left.")
        isHungry = False
    else:
        print("Invalid choice. Please choose a, b, or c.")

isBored = True

print("You finished eating the whatever you caught and now you are bored. You see a empty playground.")
        
while isBored:
    print("Choose an option:")
    print("a: You ignore the playground and go back to your comfty alleyway.")
    print("b: You go to the playground and play on the swings.")
    print("c: You go to the playground and play on the slide.")

    choice = input("Enter your choice (a, b, or c): ").lower()
            
    if choice == "a":
        print("You go back to your alleyway and take a nap in your comfy cardboard box with a warm blanket.")
        isBored = False
    elif choice == "b":
        print("You go to the playground and play happily on the swings, however you get tired after and are in need of a drink.")
        isBored = False
    elif choice == "c": 
        print("You go to the playground and are going to play on the slide, but there are two other raccoons playing on the slide already. Thankfully they are nice and they let you play on the slide with them.")
        print("You have now made two friends.")
        isBored = False
        madeFriends = True
    else:
        print("Invalid choice. Please choose a, b, or c.")
                
if madeFriends == True:
    newFriends = True
        
while newFriends:
    print("You now have two new friends, what are their names?")
    friend1 = input("Enter the name of your first friend:")
    friend2 = input("Enter the name of your second friend:")
    print(f"{friend1} and {friend2} are now your new friends.")
    newFriends = False

    isSleepy = True
                    
    while isSleepy:
        print("You are now tired from all of the playing and eating.")
        print("You rest up in your comfy cardboard box and have to choose how many hours you are going to sleep.")
        print("Choose an option:")
        print("a: You decide to sleep for a solid 8 hours")
        print("b: You decide to sleep for 4 hours")
        print("c: You are tired and decide to sleep for 10 hours")

        choice = input("Enter your choice (a, b, or c): ").lower()

        if choice == "c" and madeFriends == False:
            print("You slept for 10 hours and a random raccoon drew a moustache on your face while you were sleeping.")
            isSleepy = False

        elif choice == "c" and madeFriends == True:
            print(f"You slept for 10 hours and a random raccoon was about to draw a moustache on your face, but {friend1} and {friend2} woke you up just in time to stop them.")
            isSleepy = False
                            
        elif choice == "a":
            print("You slept for 8 hours and was able to grab a quick treat from the bakery with the time you saved.")
            isSleepy = False

        elif choice == "b":
            print("You slept for 4 hours and felt refreshed, however later in the day you got tired and had to take another nap.")
            isSleepy = False
        else:
            print("Invalid choice. Please choose a, b, or c.")

    print("BONUS ROUND:")

    print("You have been captured by the bakery owner and are now stuck in the basement of the bakery.")
    print("You have 3 doors to escape from:")

    isBonus = True

    while isBonus:
        print("Choose a door:")
        print("a: door 1")
        print("b: door 2")
        print("c: door 3")

        choice = input("Enter your choice (a, b, or c): ").lower()

        if choice == "b":
            print("You chose door 2!")
            print("You found the secret passageway to the backside of the bakery and managed to escape.")
            print("YOU WON!")
            isBonus = False

        elif choice == "a": 
            print("You chose door 1!")
            print("You opened the door to the sewers and had to find your way out, luckily after some time you ran into bob the rat and he showed you the way")
            print("You won, but there was a better way to escape.")
            isBonus = False

        elif choice == "c":
            print("You chose door 3!")
            print("You opened the door straight into the bakery owners office and he sent you right back to the basement.")
        else:
            print("Invalid choice. Please choose a, b, or c.")

    print("Thanks for playing The Great Raccoon Bakery Heist!")
