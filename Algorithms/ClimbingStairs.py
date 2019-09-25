steps1 = 2
steps2 = 3

def ClimbingStairs(n):
    if n < 3:
        return n
    prev = 1
    prev2 = 2
    for numSteps in range(3,n+1):
        current = prev + prev2
        prev = prev2
        prev2 = current
    return prev2

print(ClimbingStairs(steps1))    
print(ClimbingStairs(steps2))    