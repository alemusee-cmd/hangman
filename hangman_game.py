from hangman_functions import get_random_word, create_hidden_word
available_words = ['python', 'devops', 'jenkins', 'docker', 'kubernetes']
used_words = []
chosen = get_random_word(available_words, used_words)
game_board = create_hidden_word(chosen)
print(f"The word to guess has {len(chosen)} letters.")
print(f"Current Board: {' '.join(game_board)}")

