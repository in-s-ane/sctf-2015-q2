import sys

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

#-------------------------------------------------------------

# Find the index of all occurences of a character in the given string
def gridIndices(char, string):
    return [i for i, letter in enumerate(string) if letter == char.upper()]

#-------------------------------------------------------------
def isValid(word, used = [], startIndex = -1):
    #################################
    #debugging stuff
    print word
    print startIndex
    #print "------------------------"
    #################################
    # Base Case
    if len(word) == 1 and word in letters:
	return True

    # 1st iteration -- for 1st letter
    if startIndex == -1:
        # check if ALL letters in word are found in the grid
        for char in word:
            if char not in letters or len(gridIndices(char, letters)) < \
                                      len(gridIndices(char, word)):
                return False
        # find possible locations of first character
        indices = gridIndices(word[0], letters)
        for index in indices:
            # start path
            used.append(index)

            adjacent = get_adjacent_characters_in_grid(index)
            # if next iteration returns false
            # try another route
            # else return true
            for letter, index2 in adjacent:
                if word[1] == letter and index2 not in used:
                    used.append(index2)
                    if (isValid(word[1:], used, index2) == False):
                        used = used[:-1]
                    else:
                        return True

            # reset path
            used = []

    # next iterations -- for all letters after the first
    else:
        adjacent = get_adjacent_characters_in_grid(startIndex)
        # if next iteration returns false
        # try another route
        # else return true
        for letter, index2 in adjacent:
            if word[1] == letter and index2 not in used:
                used.append(index2)
                if (isValid(word[1:], used, index2) == False):
                    used = used[:-1]
                else:
                    return True
    return False

def main(words):
    count = 0
    for word in words:
        if isValid(word.upper()):
            count += 1
            #print word
    print count

main(words) # weird thing is when you comment out main the below isValid
# statement returns true
print isValid("aceealep".upper())
#for i in range(16):
#    print get_adjacent_characters_in_grid(i)
