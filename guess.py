import time

from colorama import Fore
def game_ran(dif):
    import random
    count = 10
    rand_num = random.randint(1,dif)
    while count != 0:
        try:
            g = int(input("Guess The Number: "))
            if g == rand_num:
                print(f"{Fore.YELLOW}You Won! The Number was: {rand_num}")
                time.sleep(2), print("Thanks you for playing"), time.sleep(2)
                return 1
            elif g < rand_num:
                print(f"{Fore.LIGHTGREEN_EX}The Number have to be higher")
            elif g > rand_num:
                print(f"{Fore.LIGHTRED_EX}The number have to be lower")
            count = count - 1
            print(f"{Fore.MAGENTA}{count} Guesses left ")
        except ValueError:
            print("Invalid Input")
    else:
        print(f"{Fore.RED}You had 10 guesses, You LOST")

