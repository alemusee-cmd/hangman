import secrets

def choose_word(available_list):
    return secrets.choice(available_list)

def update_inventory(word, available_list, used_list):
    available_list.remove(word)
    used_list.append(word)

def hidden_word(word):
    return ["_"] * len(word)

def check_len_letter(letter):
    return len(letter) == 1

def check_is_alpha(letter):
    return letter.isalpha()

def validate_input(letter):
    if check_len_letter(letter) and check_is_alpha(letter):
        return True
    return False

def count_letter_hits(letter, word):
    return word.count(letter)

def update_board(letter, word, board):
    for i, char in enumerate(word):
        if char == letter:
            board[i] = letter