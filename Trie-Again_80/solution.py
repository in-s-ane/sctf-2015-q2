import sys

sys.setrecursionlimit(20000) # yolo

letters = "EECAALEPHNBOQTTY"

# 0  1  2  3
# 4  5  6  7
# 8  9 10 11
#12 13 14 15

# E E C A
# A L E P
# H N B O
# Q T T Y

words = open("words.txt", "r").read().split("\r\n")[:-1]

# Get all characters adjacent characters at index in its row
def get_adjacent_characters_in_row(index):
    adjacent = []
    # At beginning, so we append the right
    if index % 4 == 0:
        adjacent.append([letters[index+1], index+1])
    # At end, so we append the right
    elif index % 4 == 3:
        adjacent.append([letters[index-1], index-1])
    else:
        adjacent.append([letters[index-1], index-1])
        adjacent.append([letters[index+1], index+1])
    return adjacent

# Get all adjacent characters at index
def get_adjacent_characters_in_grid(index):
    adjacent = []
    adjacent += get_adjacent_characters_in_row(index)
    if index < 4:
        adjacent += get_adjacent_characters_in_row(index+4)
        adjacent.append([letters[index+4], index+4])
    elif index < 12:
        adjacent += get_adjacent_characters_in_row(index+4)
        adjacent.append([letters[index+4], index+4])
        adjacent += get_adjacent_characters_in_row(index-4)
        adjacent.append([letters[index-4], index-4])
    else:
        adjacent += get_adjacent_characters_in_row(index-4)
        adjacent.append([letters[index-4], index-4])
    return adjacent

# Get all occurences of a character in letters
def get_all_indices(char, string):
    return [i for i, letter in enumerate(string) if letter == char]

used = []
def is_valid_word(word, index=None):
    word = word.upper()
    for char in word:
        if char not in letters or len(get_all_indices(char, letters)) < len(get_all_indices(char, word)):
            return False
    if len(word) == 1 and word in letters:
        if index:
            return word in [char for char, index in get_adjacent_characters_in_grid(index)]
        return True
    for x in range(len(word)):
        char = word[x]
        if index:
            indices = [index]
        else:
            indices = get_all_indices(char, letters)
        for index in indices:
            if index in used:
                # Can't revisit
                continue
            adjacent = get_adjacent_characters_in_grid(index)
            for letter, index2 in adjacent:
                if char == letter:
                    used.append(index)
                    return True and is_valid_word(word[x:], index2)
    return True

# count = 0
# for word in words:
#     print word
#     if is_valid_word(word):
#         count += 1

print is_valid_word("boc")
