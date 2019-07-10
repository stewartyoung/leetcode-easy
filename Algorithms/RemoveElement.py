egnums = [3,2,2,3]
egval = 3

def RemoveElement(nums, val):
	for i = 0: #range(len(nums)):
		if val == nums[i]:
			nums.pop(i)
			i = i - 1
	return len(nums)

RemoveElement(egnums, egval)
