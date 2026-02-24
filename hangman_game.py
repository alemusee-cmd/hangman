from hangman_art import draw_hangman
from hangman_functions import (
    choose_word, update_inventory, hidden_word,
    validate_input, count_letter_hits, update_board
)
available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes']
used_words = []
max_attempts = 6
errors = 0

secret_word = choose_word(available_words)
update_inventory(secret_word, available_words, used_words)
game_board = hidden_word(secret_word)

print("--- Welcome to Hangman ---")

while errors < max_attempts and "_" in game_board:
    draw_hangman(errors)
    print(f"\nBoard: {' '.join(game_board)}")
    print(f"Errors: {errors}/{max_attempts}")

    user_guess = input("Guess a letter: ").lower()

    if not validate_input(user_guess):
        print("Invalid input! Enter one letter only.")
        continue

    hits = count_letter_hits(user_guess, secret_word)

    if hits > 0:
        update_board(user_guess, secret_word, game_board)
        print(f"Yes! Found {hits} times.")
    else:
        errors += 1
        print(f"No, '{user_guess}' is not there.")

# סיום
draw_hangman(errors)
if "_" not in game_board:
    print(f"\nWinner! The word was: {secret_word}")
else:
    print(f"\nGame Over! The word was: {secret_word}")

print(f"Session history: {used_words}")