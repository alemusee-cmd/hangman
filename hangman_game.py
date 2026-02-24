from hangman_functions import get_random_word, create_hidden_word, check_guess
available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes']
used_words = []
secret_word = get_random_word(available_words, used_words)
game_board = create_hidden_word(secret_word)
print(f"Welcome! The word has {len(secret_word)} letters.")
print(f"Board: {' '.join(game_board)}")
user_guess = input("Guess a letter: ")
hits = check_guess(user_guess, secret_word, game_board)
if hits > 0:
    print(f"Yes! The letter '{user_guess}' appears {hits} times.")
else:
    print(f"Sorry, the letter '{user_guess}' is not there.")

print(f"Updated Board: {' '.join(game_board)}")

