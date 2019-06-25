nums1 = [2, 7, 11, 15]
target1 = 9


def Solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]


print(Solution(nums1, target1))
