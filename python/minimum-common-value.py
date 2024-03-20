# Time complexity O(n)
# Space complexity O(1)
def getCommon(nums1, nums2):
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        num1, num2 = nums1[i], nums2[j]
        if num1 == num2:
            return num1

        if num1 > num2:
            j += 1
        else:
            i += 1
    return -1


# Time complexity O(n)
# Space complexity O(n)
def _getCommon(nums1, nums2):
    intersection = set(nums1).intersection(set(nums2))
    return -1 if not intersection else min(intersection)
