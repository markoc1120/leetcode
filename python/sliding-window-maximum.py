from heapq import *

# Time complexity O(nlogn)
# Space complexity O(n)
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    max_heap = []
    for i in range(k):
        max_heap.append((nums[i], i))
    heapify_max(max_heap)
    
    l = 0
    ans = [max_heap[0][0]]
    for r in range(k, len(nums)):
        heappush_max(max_heap, (nums[r], r))
        l += 1

        while max_heap[0][1] < l:
            heappop_max(max_heap)
        ans.append(max_heap[0][0])

    return ans