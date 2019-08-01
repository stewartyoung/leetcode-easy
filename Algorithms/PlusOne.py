digits1 = [1,2,3]
digits2 = [4,3,2,1]

def PlusOne(digits):
    res = []
    carry = 1
    
    for d in digits[::-1]:
        res.append((d+carry)%10)
        carry = (d+carry) // 10
    
    if carry:
        res.append(carry)
        
    return res[::-1] 

print(PlusOne(digits1))
print(PlusOne(digits2))