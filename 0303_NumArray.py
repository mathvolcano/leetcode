"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._psum = self._prefix_sum()

    def sumRange(self, left: int, right: int) -> int:
        oob = 0 if left == 0 else self._psum[left -1]
        return self._psum[right] - oob

    def _prefix_sum(self):
        psum, s = [], 0
        for n in self._nums:
            s += n
            psum.append(s)
        return psum




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)