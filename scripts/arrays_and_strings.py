#!/bin/python3

"""
Practice through Cracking the Coding Interview problems in Python
"""


def isUnique(collection):
    """
    Determine if a string or list has all unique elements. Attempt to do so without any additional data structures.
    """

    # Implemented using a hash table:
    memo = set()
    for element in collection:
        if element in memo:
            return False
        memo.add(element)

    return True

    # Time Complexity: O(n)
    # Space Complexity: O(m), where m is the number of unique elements.  If this is a string with alphabetical letters, then it is going to be either 26 or 52 elements long depending on if we care about case sensitivity.


    # Implemented without additional structures
    end = len(collection)
    for i in range(end-1):
        temp_base = collection[i]
        for j in range(i + 1, end):
            if temp_base == collection[j]:
                return False

    return True

    # Time Complexity:  O(n^2)
    # Space Complexity:  O(1)


def checkPermutation(s, t):
    """
    Given two strings, determine if one is a permutation of the other.
    """

    # Count each unique letter in both strings and compare the two dicts.
    s_count = {}
    t_count = {}
    for character in s:
        s_count[character] = s_count.get(character, 0) + 1

    for character in t:
        t_count[character] = t_count.get(character, 0) + 1

    return s_count == t_count

    # Time Complexity:  O(n)
    # Space Complexity:  O(n)


def URLify(s):
    """
    Write a method to replace all spaces in a string with '%20'. Trim any spaces on the end.
    """

    # Without any additional libraries and by doing it in an array as intended by the writer.
    return ''.join('%20' if c == ' ' else c for c in s.strip())

    # Time Complexity:  O(n)
    # Space Complexity:  O(1)


def palindromePermutation(s):
    """
    Given one string, determine if it is a permutation of a palindrome.
    """
    char_count = {}
    for character in s:
        if character == ' ': continue # skip the spaces.
        char_count[character] = char_count.get(character, 0) + 1

    odd = False
    for key in char_count:
        if char_count[key] % 2 != 0:
            if odd:
                return False
            odd = True

    return True 

    # Time Complexity:  O(n)
    # Space Complexity:  O(m), where m is the number of unique characters


def oneAway(s, t):
    """
    There are three possible edits to a string: insert a character, remove a character, or replace a character.  Given two strings, write a function to check whether they are one edit or zero edits away.
    """

    # Count each unique letter in both strings and compare the two dicts.
    s_count = {}
    t_count = {}
    for character in s:
        s_count[character] = s_count.get(character, 0) + 1

    for character in t:
        t_count[character] = t_count.get(character, 0) + 1

    diffs = abs(len(s) - len(t))
    for key in s:
        diffs += abs(s_count[key] - t_count.get(key, 0))

    return diffs <= 1

    # Time Complexity:  O(len(s) + len(t))
    # Space Complexity:  O(m + n)


def stringCompression(s):
    """
    Implement a method to perform basic string compression using the counts of repeated characters, i.e. 'aabcccccaaa' --> 'a2b1c5a3'
    """

    orig_len = len(s)
    t = []
    current_letter = s[0]
    count = 1

    for i in range(1, orig_len):
        if s[i] == current_letter:
            count += 1
            if i == orig_len - 1:
                t.append(current_letter + str(count))
        else:
            t.append(current_letter + str(count))
            current_letter = s[i]
            count = 1

    t = ''.join(t)
    return t if len(t) < orig_len else s

    # Time Complexity:  O(len(s))
    # Space Complexity:  O(len(s)), worst case is 2*len(s)