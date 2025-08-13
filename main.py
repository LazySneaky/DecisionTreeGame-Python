import utilities
import paths1

def main_menu():
     paths1.slow_print("\nPlease choose an option" 
            "\nPath 1: Cave" 
            "\nPath 2: Forest")


paths1.slow_print("Welcome to the game!")


while True:

    utilities.time_sleep(1)
    main_menu()

    user_input = int(input("Choose an option: "))

    utilities.time_sleep(1)

    if user_input == 1:
        paths1.cave_way()

    elif user_input == 2:
        paths1.slow_print("not done yet")

    else:
        print("Invalid")


