import random
import time
import os

def generate_sequence(length):
    # Generate a random sequence of numbers between 1 and 9
    return [random.randint(1, 9) for _ in range(length)]

def display_sequence(sequence):
    # Display the sequence for a short duration
    for number in sequence:
        print(number, end=' ')
        time.sleep(1)
        print('\b' + ' ', end='')  # Erase the number after 1 second
        time.sleep(0.5)  # Pause for a short time before displaying the next number
    print()

def get_user_input(length):
    # Get user input for the recalled sequence
    print("Recall the sequence:")
    try:
        user_sequence = [int(input("> ")) for _ in range(length)]
        return user_sequence
    except ValueError:
        print("Invalid input. Please enter a single digit number.")
        return get_user_input(length)

def check_sequence(sequence, user_sequence):
    # Check if the user's input matches the original sequence
    return sequence == user_sequence

def memory_game(difficulty):
    sequence_length = difficulty
    original_sequence = generate_sequence(sequence_length)

    # Display the sequence to the player
    print("Memorize the sequence:")
    display_sequence(original_sequence)

    # Clear the console after displaying the sequence
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get the user's input for the recalled sequence
    user_sequence = get_user_input(sequence_length)

    # Check if the input matches the original sequence
    if check_sequence(original_sequence, user_sequence):
        print("Congratulations! You remembered the sequence.")
        return 1  # Return 1 for success
    else:
        print("Incorrect sequence. Better luck next time.")
        return 0  # Return 0 for failure

