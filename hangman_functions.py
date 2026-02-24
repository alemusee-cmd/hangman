import secrets

def choose_word(available_list):
    return secrets.choice(available_list)

def remove_from_available(word, available_list):
    available_list.remove(word)

def add_to_used(word, used_list):
    used_list.append(word)

def create_board(word):
    return ["_"] * len(word)

def is_length_valid(letter):
    return len(letter) == 1

def is_letter(letter):
    return letter.isalpha()

def validate_input(letter):
    return is_length_valid(letter) and is_letter(letter)

def count_hits(letter, word):
    return word.count(letter)

def reveal_letters(letter, word, board):
    for i, char in enumerate(word):
        if char == letter:
            board[i] = letter

def check_win(board):
    return "_" not in board