egnums = [3,2,2,3]
egval = 3

def RemoveElement(nums, val):
	i = 0 #range(len(nums)):
	for num in nums:
		if num != val:
			nums[i] = num
			i += 1
	return i

print(RemoveElement(egnums, egval))
