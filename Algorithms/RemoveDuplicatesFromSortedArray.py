egNums1 = [1,1,2]
egNums2 = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums) -> int:
	uniqueSet = []
	for number in nums:
		if number not in uniqueSet:
			uniqueSet.append(number)
	return uniqueSet

print(removeDuplicates(egNums1))
print(removeDuplicates(egNums2))
