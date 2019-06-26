example1 = "III"
example2 = "IV"


def romanToInt(s: str) -> int:
    number = 0
    for character in range(0, len(s)):
        if s[character] == "I":
            number += 1
        elif s[character] == "V":
            number += 5
        elif s[character] == "X":
            number += 10
        elif s[character] == "L":
            number += 50
        elif s[character] == "C":
            number += 100
        elif s[character] == "D":
            number += 500
        elif s[character] == "M":
            number += 1000
            return number


print(romanToInt(example1))
print(romanToInt(example2))
