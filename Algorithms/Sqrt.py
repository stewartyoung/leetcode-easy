eg1 = 4
eg2 = 81

def Sqrt(x):
    r = x + 1 # avoid infite loop by avoiding dividing by 0
    while r*r>x:
        r = int(r-(r*r - x)/(2*r))
    return r

print(Sqrt(eg1))
print(Sqrt(eg2))