egnums1 = [1,2,3,0,0,0]
egm = 3
egnums2 = [2,5,6]
egn = 3

#  m is length of nums1, n length of nums2
def MergeSortedArray(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    print(nums1)

MergeSortedArray(egnums1, egm, egnums2,egn)

