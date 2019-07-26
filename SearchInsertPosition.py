sortedArray1 = [1,3,5,6]
target1 = 5
sortedArray2 = [1,3,5,6]
target2 = 2
sortedArray3 = [1,3,5,6]
target3 = 7
sortedArray4 = [1,3,5,6]
target4 = 0

def SearchInsertPosition(nums, target):
        for i in nums:
            if i >= target:
                return nums.index(i)
        return len(nums)

print(SearchInsertPosition(sortedArray1, target1))
print(SearchInsertPosition(sortedArray2, target2))
print(SearchInsertPosition(sortedArray3, target3))
print(SearchInsertPosition(sortedArray4, target4))