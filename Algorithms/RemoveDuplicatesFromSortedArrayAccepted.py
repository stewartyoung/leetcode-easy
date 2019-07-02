egNums1 = [1,1,2]
egNums2 = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
	count = 0
	for number in nums:
		if count == 0 or number != nums[count - 1]:
			nums[count] = number
			count += 1
	return count

print(removeDuplicates(egNums1))
print(removeDuplicates(egNums2))
