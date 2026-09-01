print("The Great Raccoon Bakery Heist")
print("You are a hungry Raccoon standing in the dark alley behind a bakery in the middle of the night. You smell fresh croissants.")

newFriends = False

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
        print("You climb smoothly climb through the window and the guard is still asleep, however you knock over the tray of crossaints and the guard wakes up and chases you down.")
        isHungry = False
    elif choice == "b":
        print("You sneak through the back door and manage to avoid the alarms and the guard, but you took too long and all the crossaints are gone and there's only a mere slice of bread left.")
        isHungry = False

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
                        print("a:")

                

                 
                
