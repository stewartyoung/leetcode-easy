eg1="()"
eg2="()[]{}"
eg3="(]"
eg4="(([)]"
eg5="{[]}"


def isValid(self, s: str) -> bool:
        if s is None:
            return
      
        brackets = {"[" : "]", "{" : "}", "(" : ")"}
        stack = []
        
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            elif len(stack) != 0 and stack.pop() == bracket:
                continue
            else:
                return False
        
        return len(stack) == 0

print(isValid(eg1))
print(isValid(eg2))
print(isValid(eg3))
print(isValid(eg4))
print(isValid(eg5))
