import random
def get_random_word(available_words, used_words):
    index = random.randint(0, len(available_words) - 1)
    chosen_word = available_words.pop(index)
    used_words.append(chosen_word)
    return chosen_word

def create_hidden_word(word):
    return ["_"] * len(word)

def check_guess(guess, secret_word, current_board):
    count = 0
    for index, letter in enumerate(secret_word):
        if letter == guess:
            current_board[index] = guess
            count += 1
    return count