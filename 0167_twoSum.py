"""
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) time and O(1) (excluding input), including input O(n)
        n = len(numbers)
        if n == 2: return [1,2]

        l, r = 0, n - 1
        cur = numbers[l] + numbers[r]
        while cur != target:
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            cur = numbers[l] + numbers[r]
        return [l+1, r+1]

        # Binary Search
        # n = len(numbers)
        # for i in range(n):
        #     l, r = i + 1, n - 1
        #     diff = target - numbers[i]
        #     while l <= r:
        #         m = l + (r-l)//2
        #         if numbers[m] == diff:
        #             return [i+1, m+1]
        #         elif numbers[m] < diff:
        #             l = m + 1
        #         else:
        #             r = m - 1