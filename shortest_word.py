""" Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types."""

def find_short(s):
    length_list = []
    word_list = s.split(' ')
    for word in word_list:
        length_list.append(len(word))
    return min(length_list)

print(find_short("String will never be empty"))