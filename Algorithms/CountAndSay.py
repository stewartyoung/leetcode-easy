import re

in1 = 1
in2 = 4


def countAndSay(n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

print(countAndSay(in1))
print(countAndSay(in2))