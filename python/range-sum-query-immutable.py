# Time complexity O(n) - initialization, otherwise O(1)
# Space complexity O(n)
class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0]
        for i, num in enumerate(nums, 1):
            self.prefix_sum.append(num + self.prefix_sum[i - 1])

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
