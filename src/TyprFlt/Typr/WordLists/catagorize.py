import os
def categorize_words(input_file, output_home_row, output_top_row, output_bottom_row):
    home_row = set('asdfghjkl')
    top_row = set('qwertyuiop')
    bottom_row = set('zxcvbnm')

    home_row_words = []
    top_row_words = []
    bottom_row_words = []

    with open(input_file, 'r') as infile:
        for line in infile:
            word = line.strip().lower()
            row_set = None

            if all(c in home_row for c in word):
                row_set = home_row_words
            elif all(c in top_row for c in word):
                row_set = top_row_words
            elif all(c in bottom_row for c in word):
                row_set = bottom_row_words

            if row_set is not None:
                row_set.append(word)

    append_to_file(output_home_row, home_row_words)
    append_to_file(output_top_row, top_row_words)
    append_to_file(output_bottom_row, bottom_row_words)

def append_to_file(output_file, words):
    mode = 'a' if os.path.exists(output_file) else 'w'
    with open(output_file, mode) as outfile:
        outfile.write('\n'.join(words) + '\n')

# Example usage:

input_file = 'Master_EN_Word_List.txt'
output_home_row = 'Home_Row_Words.txt'
output_top_row = 'Top_Row_Words.txt'
output_bottom_row = 'Bottom_Row_Words.txt'

categorize_words(input_file, output_home_row, output_top_row, output_bottom_row)

