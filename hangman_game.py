from hangman_art import draw_hangman
from hangman_functions import *
available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes']
used_words = []
errors = 0
max_errors = 6

word = choose_word(available_words)
remove_from_available(word, available_words)
add_to_used(word, used_words)
board = create_board(word)

print("--- Game Started ---")

while errors < max_errors and not check_win(board):
    draw_hangman(errors)
    print(f"Board: {' '.join(board)} | Errors: {errors}/{max_errors}")
    guess = input("Enter a letter: ").lower()
    if not validate_input(guess):
        print("Invalid! One letter only.")
        continue

    hits = count_hits(guess, word)
    if hits > 0:
        reveal_letters(guess, word, board)
        print(f"Yes! {hits} hits.")
    else:
        errors += 1
        print("No luck!")

draw_hangman(errors)
if check_win(board):
    print(f"Winner! Word: {word}")
else:
    print(f"Game Over! Word: {word}")