haystack1 = "hello"
haystack2 = "aaaaa"
needle1 = "ll"
needle2 = "bba"

def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) +1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr(haystack1, needle1))
print(strStr(haystack2, needle2))