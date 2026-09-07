import random
import hangman_methods
import list_of_words

blank_spaces_and_letters = []
all_user_guesses = []

user_lives = 5
continue_request = True


if __name__ == "__main__":
    hangman_methods.hangman_introduction()

    while continue_request:
        computer_word = random.choice(list_of_words.all_words)
        hangman_methods.add_blank_spaces(computer_word, blank_spaces_and_letters)

        while user_lives > 0:
            hangman_methods.display_blank_spaces(blank_spaces_and_letters)

            user_guess = input("Guess a letter: ")
            user_guess = user_guess.lower()

            # Confirm if the user already guessed a letter
            # If so, notify the user and continue the loop at the top
            # Otherwise, the letter is added to a master list
            if hangman_methods.check_for_valid_guess(user_guess, all_user_guesses):
                print("You already guessed that letter!\n")
                continue
            else:
                all_user_guesses.append(user_guess)

            # Checks if the user's guess is in the computer word, and if so, update the blank_spaces list
            if user_guess in computer_word:
                print("You got it!\n")
                hangman_methods.update_blank_spaces_list(computer_word, user_guess, blank_spaces_and_letters)
            else:
                user_lives = hangman_methods.modify_lives(user_lives)
                print(f"Nope! You lost a life ({user_lives} lives remaining)\n")

            # Check if there are any blank spaces remaining in the blank_spaces list
            # If there are, continue the game
            # Otherwise, exit the loop
            if "_" in blank_spaces_and_letters:
                continue
            else:
                break

        # Ternary check for game status
        print(f"You {'won' if user_lives > 0 else 'lost'}! The word was {computer_word}\n")

        # Continue loop
        continue_request = hangman_methods.continue_game_selection(blank_spaces_and_letters, all_user_guesses, user_lives)
        if continue_request:
            user_lives = 5

        print(f"{"Let's play!" if continue_request else "Bye!"}\n")