# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# To solve this problem, we can create a dictionary to count the number of occurrences of each character in the string s. Then, we can iterate through the characters in the string t and decrement the count for each character in the dictionary. If the count for any character becomes negative, it means that there are more occurrences of that character in t than in s, so we can return false immediately. If we finish iterating through t and the counts for all characters are non-negative, it means that t is an anagram of s, so we can return true.

# Here is the modified code that implements this approach:


def isAnagram(s, t):
    # Create a dictionary to count the number of occurrences of each character in s
    s_counts = {}
    for ch in s:
        if ch in s_counts:
            s_counts[ch] += 1
        else:
            s_counts[ch] = 1

    # Iterate through the characters in t and decrement the count for each character in the dictionary
    for ch in t:
        if ch in s_counts:
            s_counts[ch] -= 1
            if s_counts[ch] < 0:
                # If the count for a character becomes negative, t is not an anagram of s
                return False
        else:
            # If a character in t is not in the dictionary, t is not an anagram of s
            return False

    # If we finish iterating through t and the counts for all characters are non-negative, t is an anagram of s
    return True


# This should correctly determine whether t is an anagram of s for the given input.


# I don't clearly understand it properly. Can you add more explanation?
# Certainly! Here is a more detailed explanation of the code:

# First, we create a dictionary called s_counts that will keep track of the number of occurrences of each character in the string s. We iterate through the characters in s and update the count for each character in the dictionary. If a character is not in the dictionary, we add it to the dictionary with a count of 1. If it is already in the dictionary, we increment its count by 1.

# Next, we iterate through the characters in the string t. For each character, we check if it is in the s_counts dictionary. If it is, we decrement its count by 1. If the count for a character becomes negative, it means that there are more occurrences of that character in t than in s, so we return False immediately. If a character in t is not in the s_counts dictionary, it means that it does not occur in s, so we return False immediately.

# If we finish iterating through t and the counts for all characters in the s_counts dictionary are non-negative, it means that t is an anagram of s, so we return True.

# I hope this helps clarify things. Let me know if you have any more questions.


# why do we decrement?
# We decrement the count for each character in t in the s_counts dictionary to keep track of the number of occurrences of that character in s that have not been matched with an occurrence in t. This allows us to determine whether t is an anagram of s by ensuring that the counts for all characters in s are non-negative after we have processed all the characters in t.

# For example, consider the strings s and t:

# Copy code
# s = "abc"
# t = "bca"
# We create the s_counts dictionary with counts for each character in s:


# s_counts = {
#     "a": 1,
#     "b": 1,
#     "c": 1
# }
# We then iterate through the characters in t and decrement the count for each character in the s_counts dictionary:

# Copy code
# s_counts = {
#     "a": 0,  # count for "a" is decremented to 0
#     "b": 0,  # count for "b" is decremented to 0
#     "c": 0   # count for "c" is decremented to 0
# }
# After we have processed all the characters in t, the counts for all characters in s_counts are 0, which means that t is an anagram of s. If any of the counts had been negative after processing all the characters in t, it would mean that there are more occurrences of that character in t than in s, so t would not be an anagram of s.

