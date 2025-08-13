import utilities


def slow_print(text, speed=0.06):  # Lower number = faster
    for letter in text:
        print(letter, end='', flush=True)
        utilities.time.sleep(speed)
    print()




def cave_way():
    print("You have entered the cave")
    utilities.time_sleep(0.5)

    slow_print("Where do you want to go?"
          "\n1: Go deeper"
          "\n2: Go to start point")
    utilities.time_sleep(1)
    user_input2 = int(input("Choose:"))

    if user_input2 == 1:
        utilities.time_sleep(0.5)        
        slow_print("You went deeper in the cave and encountered a dragon!")
        slow_print("1: Run!" \
              "\n2: Fight it!")
        utilities.time_sleep(1)

        user_input3 = int(input("Enter your choice: "))

        if user_input3 == 2:
            slow_print("LMAOO trying to be a hero.. ")
            utilities.time_sleep(0.5)
            slow_print("You're dead!")
            return
        elif user_input3 == 1:
            slow_print("Good choice!")
        

    elif user_input2 == 2:
        utilities.time_sleep(2)
        return
        