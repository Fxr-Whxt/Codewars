'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''


def find_short(s):
    s = sorted(s.split(), key=len)
    for i in list(s):
        l = [i]
        return len(l[0])