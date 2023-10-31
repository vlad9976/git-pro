import random
from colorama import Fore
def rock_game(till):
    Pccount = 0
    Usercount = 0
    while True:
        choice = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choice)
        try:
            user_input = input(f"Choose Rock ,Paper ,Scissors: ")
            if user_input not in choice:
                print(f"{Fore.RED}Unavailable Input")
            elif user_input == computer:
                print(f"{Fore.LIGHTBLUE_EX}Same")
            elif user_input == "Rock" and computer == "Scissors":
                Usercount += 1
                print(f"Your choice: {Fore.LIGHTGREEN_EX}{user_input}\nComputer Choice: {Fore.LIGHTRED_EX}{computer}\n{Fore.GREEN}Great You WON!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
            elif computer == "Rock" and user_input == "Scissors":
                Pccount += 1
                print(f"Your choice: {user_input}\nComputer Choice: {computer}\nLOOSEERR!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
            elif user_input == "Paper" and computer == "Rock":
                Usercount += 1
                print(f"Your choice: {user_input}\nComputer Choice: {computer}\nGreat You WON!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
            elif computer == "Paper" and user_input == "Rock":
                Pccount += 1
                print(f"Your choice: {user_input}\nComputer Choice: {computer}\nLOOSEERR!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
            elif user_input == "Scissors" and computer == "Paper":
                print(f"Your choice: {user_input}\nComputer Choice: {computer}\nGreat You WON!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
                Usercount += 1
            elif computer == "Scissors" and user_input == "Paper":
                print(f"\nYour choice: {user_input}\nComputer Choice: {computer}\nLOOSEERR!\nYour Score: {Usercount}\nComputer Score: {Pccount}")
                Pccount += 1
        except ValueError:
            print("Invalid Input")
        if Usercount == till:
            print("You WON!!!\n"
                  "=== End Game ===")
            return 1
        elif Pccount == till:
            print("You Lost!!!\n=== End Game ===")
            break


