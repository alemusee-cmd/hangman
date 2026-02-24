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


import os


def load_users(filename="users.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def save_user(username, filename="users.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")


def handle_user_login():
    users = load_users()
    name = input("Enter your name: ").strip()

    if name in users:
        print(f"Welcome back, {name}!")
    else:
        print(f"Welcome, {name}! You have been registered as a new user.")
        save_user(name)
    return name