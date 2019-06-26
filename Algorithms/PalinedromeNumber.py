example1 = 121  # Should return true
example2 = -121  # Should return false
example3 = 1000021  # Should return true


def PalinedromeNumber(x: int) -> bool:
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False


print(PalinedromeNumber(example1))
print(PalinedromeNumber(example2))
print(PalinedromeNumber(example3))
