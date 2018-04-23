# File : Lagunitas application assessment
# Author : Charlie Moore
# Description : Functions written for the Lagunitas assessment
#               Written in Python version 3.4.3

from collections import Counter, Iterable


def stringCounter(userText):
    # Input:  String of words
    # Output: Counter container object containing tallied values for the number
    #         of times a word appears in the string
    stringTallies = Counter()
    words = userText.split()
    for word in words:
        stringTallies[word] += 1
    return stringTallies


def flattenList(unflat):
    # Input:  A nested list
    # Output: A list containing only non-list elements
    return list(flatListGenerator(unflat))


def flatListGenerator(unflat):
    # Input:  A nested list
    # Output: Object which generates a flat list
    for elem in unflat:
        if isinstance(elem, Iterable) and not isinstance(elem, (str, bytes)):
            yield from flatListGenerator(elem)
        else:
            yield elem


def main():
    # Test string counting
    userText = str(input("Enter some text:"))
    tallies = stringCounter(userText)
    print(tallies)

    # Test list flattening
    unflatlist = [['a','b'],'c',[[4,5],6],7]
    flatlist = flattenList(unflatlist)
    print(unflatlist)
    print(flatlist)


main()
