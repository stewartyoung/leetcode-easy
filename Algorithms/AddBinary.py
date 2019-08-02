a1 = "11"
b1 = "1"
a2 = "1010"
b2 = "1011"

def AddBinary(a,b):
    result = ''
    index = 0

    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'

        val = int(num_a) + int(num_b) + int(carry)
        result = str(val % 2) + result

        carry = '1' if val > 1 else '0'
        index += 1

    return result

print(AddBinary(a1,b1))
print(AddBinary(a2,b2))