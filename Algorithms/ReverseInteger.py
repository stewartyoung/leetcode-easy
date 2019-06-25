example1 = 123
example2 = -123
example3 = 120


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 2**31-1 or x <= -2**31:
        return 0
    else:
        string = str(x)
        if x >= 0:
            """
            If number is positive use a slice statement that steps backwards, [::-1], is the same as [2:0:-1] which means start at position 2 (because "123" has 3 characters), end at position 0, move with the step -1, negative one, which means one step backwards.
            """
            reversedString = string[::-1]
        else:
            # If number is negative, ignore first digit
            stringNoNegative = string[1:]
            stringNoNegativeReversed = stringNoNegative[::-1]
            reversedString = "-" + stringNoNegativeReversed
        if int(reversedString) >= 2**31-1 or int(reversedString) < - 2**31:
            return 0
        else:
            return int(reversedString)


print(reverse(example1))
print(reverse(example2))
print(reverse(example3))
