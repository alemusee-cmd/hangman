from hangman_functions import get_random_word, create_hidden_word, check_guess, validate_input
available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes']
used_words = []
max_attempts = 6
errors = 0
secret_word = get_random_word(available_words, used_words)
game_board = create_hidden_word(secret_word)
print("--- Welcome to the Hangman DevOps Challenge! ---")
print(f"The word has {len(secret_word)} letters.")
while errors < max_attempts and "_" in game_board:
    print(f"\nBoard: {' '.join(game_board)}")
    print(f"Errors: {errors}/{max_attempts}")

    user_guess = input("Guess a letter: ").lower()
    if not validate_input(user_guess):
        continue
    hits = check_guess(user_guess, secret_word, game_board)

    if hits > 0:
        print(f"Nice! '{user_guess}' appears {hits} times.")
    else:
        errors += 1
        print(f"Oops! The letter '{user_guess}' is not in the word.")
if "_" not in game_board:
    print(f"\nCongratulations! You won! The word was: {secret_word}")
else:
    print(f"\nGame Over! You've been hanged. The word was: {secret_word}")
print(f"\nWords played in this session: {used_words}")

