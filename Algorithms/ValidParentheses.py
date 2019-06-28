eg1="()"
eg2="()[]{}"
eg3="(]"
eg4="(([)]"
eg5="{[]}"


def isValid(string: str) -> bool:
	# if string doesn't exist, return nothing
        if string is None:
            return
      
        brackets = {
			"[" : "]", 
			"{" : "}", 
			"(" : ")"
			}

		#stack is just a list, but it needs to be operated as LIFO (last in first out)
        stack = []
        
        for bracket in string:
            if bracket in brackets:
				# if the open bracket is in the brackets dictionary, append all the closing brackets of the opening brackets to the stack
                stack.append(brackets[bracket])

				# if the stack contains something, and the bracket popped off (the closing bracket) is equal to opening bracket
            elif len(stack) != 0 and stack.pop() == bracket:
                continue
            else:
                return False
        
		# If stack is empty, all brackets have been closed, and so return true as parens are valid
        return len(stack) == 0

print(isValid(eg1))
print(isValid(eg2))
print(isValid(eg3))
print(isValid(eg4))
print(isValid(eg5))
