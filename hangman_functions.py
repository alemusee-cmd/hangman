import random
def get_random_word(available_words, used_words):
    index = random.randint(0, len(available_words) - 1)
    chosen_word = available_words.pop(index)
    used_words.append(chosen_word)
    return chosen_word

def create_hidden_word(word):
    return ["_"] * len(word)