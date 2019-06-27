stringList1 = ["flower", "flow", "flight"]
stringList2 = ["dog", "racecar", "car"]

def longestCommonPrefix(stringList) -> str:
        # If string list doesn't contain anything, return empty string
        if not stringList: 
            return ''
        
        # Take the last item in the stringList
        lastItem = min(stringList)
        
        # For character in (0,len of last item)
        for char in range(len(lastItem)):
            
            # For string in string list
            for string in stringList:
                
                # If strings character doesn't equal last items character at same index
                if string[char] != lastItem[char]:
                    
                    # return the string up to one before the character being examined, if its the first letter being compared return empty string
                    return lastItem[:char] if char > 0 else ''
                
        # If we manage to get through the whole string return lastItem        
        return lastItem

print(longestCommonPrefix(stringList1))
print(longestCommonPrefix(stringList2))
