example1 = 121  # Should return true
example2 = -121  # Should return false


def PalinedromeNumber(x: int) -> bool:
    string = str(x)
    if string[0] == string[-1]:
        return True
    else:
        return False


print(PalinedromeNumber(example1))
print(PalinedromeNumber(example2))
