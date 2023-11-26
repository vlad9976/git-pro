
import time
from colorama import Fore

from guess import game_ran
from mem_game import memory_game
from rock_paper import rock_game
from Score import add_score
from run_app import stop_flask_server
from utils import cls_screen, load_game_assets



def Welcome():  # Ask for a name.
    name = input("Enter your name: ")
    print(f'''{Fore.RED}Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.
Flask Server Running in background.
You can find your score here --> http://127.0.0.1:5000/''')
    load_game(name)


def load_game(name):  # Load game (With parameter name from Welcome())
    game_1 = "1. Guess Game - Guess a number and see if you chose like the computer"
    game_2 = "2. Memory Game - A sequence of numbers will appear for and you have to guess it back"
    game_3 = "3. Rock,Paper,Scissors Game - Lets see if you can beat the computer"
    stop_web = "To stop the web server just press 'stop'"
    print("Please choose a game to play")
    print(f"{Fore.BLUE}{game_1}\n{game_2}\n{game_3}\n{Fore.RED}{stop_web}")

    # Saves user game and difficulty.
    user_game = "Game: "
    difficulty = "Difficulty: "
    # Ask user to choose a number 1-3

    a = input("Choose a number 1, 2, 3: ")
    if a.lower() == "stop":
        # Stop the web server
        stop_flask_server()
    elif a.isdigit():
        a = int(a)
        while a > 4 or a < 1:
            print("The input should be a number between 1 to 3 OR 'stop':")
            a = int(input("Choose a number 1, 2, 3: "))
    # ============= game 1 Guess-Game=============
    if a == 1:
        diff = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
        print(Fore.GREEN + game_1)
        b = int(input("Please choose game difficulty from 1 to 5: "))
        while b > 5 or b < 1:
            print("the input suppose to be a number between 1 to 5")
            b = int(input("Please choose game difficulty from 1 to 5: "))
        difficulty = difficulty + str(b)
        user_game = user_game + str(a)
        print(f"{user_game}, {difficulty}")
        f"{Fore.CYAN} {load_game_assets()}"
        time.sleep(1), cls_screen()
        if b == 1:
            print("Hello This is a Guessing game you have 10 guesses, Guess Number 1-20")
        elif b == 2:
            print("Hello This is a Guessing game you have 10 guesses, Guess Number 1-40")
        elif b == 3:
            print("Hello This is a Guessing game you have 10 guesses, Guess Number 1-60")
        elif b == 4:
            print("Hello This is a Guessing game you have 10 guesses, Guess Number 1-80")
        elif b == 5:
            print("Hello This is a Guessing game you have 10 guesses, Guess Number 1-100")
        if game_ran(diff[b]) == 1:
            add_score(name, b)
    # ============= game 2 Memory-Game=============
    elif a == 2:
        print(Fore.GREEN + game_2)
        diff = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
        b = int(input("Please choose game difficulty from 1 to 5: "))
        while b > 5 or b < 1:
            print("the input suppose to be a number between 1 to 5")
            b = int(input("Please choose game difficulty from 1 to 5: "))
        difficulty = difficulty + str(b)
        user_game = user_game + str(a)
        print(f"{user_game}, {difficulty}")
        f"{Fore.CYAN} {load_game_assets()}"
        time.sleep(1), cls_screen()
        if b == 1:
            print("Hello This is a Memory Game, Difficulty level 1 (2 characters)")
        elif b == 2:
            print("Hello This is a Memory Game, Difficulty level 2 (4 characters)")
        elif b == 3:
            print("Hello This is a Memory Game, Difficulty level 3 (6 characters)")
        elif b == 4:
            print("Hello This is a Memory Game, Difficulty level 4 (8 characters)")
        elif b == 5:
            print("Hello This is a Memory Game, Difficulty level 5 (10 characters)")
        if memory_game(diff[b]) == 1:
            add_score(name, b)
    # ============= game 3 Rock,Paper,Scissors Game=============
    elif a == 3:
        diff = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        print(Fore.GREEN + game_3)
        b = int(input("Please choose game difficulty from 1 to 5: "))
        while b > 5 or b < 1:
            print("the input suppose to be a number between 1 to 5")
            b = int(input("Please choose game difficulty from 1 to 5: "))
        difficulty = difficulty + str(b)
        user_game = user_game + str(a)
        print(f"{user_game}, {difficulty}")
        f"{Fore.CYAN} {load_game_assets()}"
        time.sleep(1), cls_screen()
        if b == 1:
            print("Hello This is a Rock,Paper,Scissors Game, Difficulty level 1 (Till 1)")
        elif b == 2:
            print("Hello This is a Rock,Paper,Scissors Game, Difficulty level 2 (Till 2)")
        elif b == 3:
            print("Hello This is a Rock,Paper,Scissors Game, Difficulty level 3 (Till 3)")
        elif b == 4:
            print("Hello This is a Rock,Paper,Scissors Game, Difficulty level 4 (Till 4)")
        elif b == 5:
            print("Hello This is a Rock,Paper,Scissors Game, Difficulty level 5 (Till 5)")
        if rock_game(diff[b]) == 1:
            add_score(name, b)
    # ======================Stop Web Server=======================
    elif a == "stop":
        print("Flask server stopping...You will not see your score anymore")
        stop_flask_server()
    else:
        print("\n!!!!!!!!!!You have to choose between 1-3 OR stop!!!!!!!!!!\n")
        load_game(name)
    cls_screen()
    load_game(name)
