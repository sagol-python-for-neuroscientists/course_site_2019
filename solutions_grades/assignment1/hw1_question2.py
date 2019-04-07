"""
__author__ = Hagai Har-Gil
HW1 Question 2 Solution
"""
# Question 2
def is_palindrome(seq):
    return seq == seq[::-1]


def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    result = []
    for num in range(100000, 1000000):
        if (
            is_palindrome(str(num)[2:])
            and is_palindrome(str(num + 1)[1:])
            and is_palindrome(str(num + 2)[1:5])
            and is_palindrome(str(num + 3))
        ):

            result.append(num)

    return result


if __name__ == "__main__":
    print("Question 2 solution:")
    fitting_numbers = check_palindrome()
    print(fitting_numbers)

