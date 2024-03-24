# Time complexity O(n)
# Space complexity O(n)
def pivotIndex(nums):
    prefix_sum = [0]
    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])

    for i in range(len(nums)):
        if prefix_sum[i] == prefix_sum[-1] - prefix_sum[i + 1]:
            return i
    return -1


# Time complexity O(n)
# Space complexity O(1)
def _pivotIndex(nums):
    prefix_sum, total = 0, sum(nums)
    for i, num in enumerate(nums):
        if prefix_sum == total - prefix_sum - num:
            return i
        prefix_sum += num
    return -1
