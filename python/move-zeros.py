# Time complexity O(n)
# Space complexity O(1)
def moveZeroes(nums):
    last_non_zero = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    return nums
