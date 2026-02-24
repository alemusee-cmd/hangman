from hangman_functions import get_random_word, create_hidden_word, check_guess, validate_input, HANGMAN_PICS

available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes', 'terraform', 'ansible']
used_words = []
max_attempts = 6
errors = 0

secret_word = get_random_word(available_words, used_words)
game_board = create_hidden_word(secret_word)

print("--- Welcome to Hangman ---")

while errors < max_attempts and "_" in game_board:
    # כאן אנחנו מדפיסים את המשתנה - בלי גרשיים!
    print(HANGMAN_PICS[errors])
    print(f"\nBoard: {' '.join(game_board)}")
    print(f"Errors: {errors}/{max_attempts}")

    user_guess = input("Guess a letter: ").lower()

    if not validate_input(user_guess):
        continue

    hits = check_guess(user_guess, secret_word, game_board)

    if hits > 0:
        print(f"Yes! '{user_guess}' appears {hits} times.")
    else:
        errors += 1
        print(f"No, '{user_guess}' is not there.")

# סיום המשחק
if "_" not in game_board:
    print(HANGMAN_PICS[errors])
    print(f"\nWinner! The word was: {secret_word}")
else:
    print(HANGMAN_PICS[errors])
    print(f"\nGame Over! The word was: {secret_word}")

print(f"Played words: {used_words}")