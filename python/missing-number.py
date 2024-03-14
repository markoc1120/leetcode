# Time complexity O(n)
# Space complexity O(n)
def missingNumber(nums):
    seen = set(nums)
    for i in range(len(nums) + 1):
        if i not in seen:
            return i


# Time complexity O(n)
# Space complexity O(1)
def _missingNumber(nums):
    return (len(nums) * len(nums) + 1) / 2 - sum(nums)
