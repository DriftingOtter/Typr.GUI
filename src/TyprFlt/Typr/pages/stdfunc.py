import string
import random

def generate_challenge_text(num_of_words, word_list_path):
    challenge_text = []
    
    with open(word_list_path, "r") as current_text:
        lines = current_text.readlines()

    num_lines = len(lines)

    for _ in range(num_of_words):
        random_line_gen = random.randint(0, num_lines - 1)
        challenge_text.append(lines[random_line_gen].strip())

    return challenge_text

def conv_lts(lst):
    str_text = " ".join(map(str, lst))
    str_text = str_text.translate({ord(c): " " for c in string.whitespace})

    return str(str_text)

