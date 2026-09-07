import time

def hangman_introduction():
    print("Welcome to hangman!")
    time.sleep(1)
    print("Allow me to select a word...")
    time.sleep(3)
    print("I've got it! Let's play hangman!\n")
    time.sleep(2)

def add_blank_spaces(computer_word, blank_spaces_and_letters):
    for letter in computer_word:
        blank_spaces_and_letters.append("_")

def display_blank_spaces(blank_spaces_and_letters):
    for char in blank_spaces_and_letters:
        print(char, end=" ")

    print()

def check_for_valid_guess(letter, all_user_guesses):
    if letter in all_user_guesses:
        return True
    else:
        return False

def update_blank_spaces_list(computer_word, user_guess, blank_spaces_and_letters):
    indexes = [index for index, letter in enumerate(computer_word) if letter == user_guess]
    for idx in indexes:
        blank_spaces_and_letters[idx] = user_guess

def reset_game(blank_spaces_and_letters, all_user_guesses):
    blank_spaces_and_letters.clear()
    all_user_guesses.clear()
    print()

def modify_lives(user_lives):
    return user_lives - 1

def continue_game_selection(blank_spaces_and_letters, all_user_guesses, user_lives):
    while True:
        continue_choice = input("Do you want to play again? (y/n): ")
        continue_choice = continue_choice.lower()

        if continue_choice == 'y':
            reset_game(blank_spaces_and_letters, all_user_guesses)
            return True
        elif continue_choice== 'n':
            return False
        else:
            print("Please enter 'y' or 'n': ")