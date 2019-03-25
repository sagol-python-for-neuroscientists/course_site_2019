"""
__author__ = Hagai Har-Gil
HW1 Question 1 Solution

This is by far not the fastest solution, but I wanted to show
you how I divide the question into a main function (trifeca)
and a smaller function (_trifeca_logic) that does the "heavy
lifting".
"""

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    if len(word) < 6:
        return False

    first_letters = word[::2]
    second_letters = word[1::2]
    # Deal with pairs starting in an even letter
    if _trifeca_logic(first_letters, second_letters):
        return True
    # If we reached here we need to deal with the case of a pair of letters starting in an odd letter
    else:
        return _trifeca_logic(first_letters[1:], second_letters)


def _trifeca_logic(firsts, seconds):
    """
    Iterate over pairs of letters, counting the number
    of consecutrive pairs.
    firsts and seconds are strings.
    """
    num_pairs = 0
    for first, second in zip(firsts, seconds):
        if first == second:
            num_pairs += 1
            if num_pairs == 3:
                return True
        else:
            num_pairs = 0
    return False


if __name__ == "__main__":
    print("Question 1 solution:")
    strings = ["aabbcc", "llkkbmm", "434343", "abccddee0123", "aaaazz", "bbcCdd", ""]
    ground_truth = [True, False, False, True, True, False, False]
    for string, truth in zip(strings, ground_truth):
        print(
            f"For the string {string}, my function returned {trifeca(string)} while the real answer is {truth}."
        )

