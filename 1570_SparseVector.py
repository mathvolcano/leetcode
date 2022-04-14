"""
1570. Dot Product of Two Sparse Vectors
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        # 2 pointer solution with Binary search
        # [1] Store the indices & values together as a tuple
        # [2] in dotproduct, have 2 pointers to next index and increment if indices disagree, if they agree multiply
        # and add to result
        # Worst case O(len(nums)) time complexity and space to create & store tuples
        # Dot product: if n & m are the lengths of self.indices for nums & vec respectively then
        # time complexity is O(max(n log m, m log n))
        import bisect
        self.indices, self.values = [], []
        for i,v in enumerate(nums):
            self.indices.append(i)
            self.values.append(v)

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i = j = 0
        while i < len(self.indices) and j < len(vec.indices):
            if self.indices[i] == vec.indices[j]:
                res += self.values[i] * vec.values[j]
                i += 1
                j += 1
            elif i < j:
                i = bisect.bisect_left(self.indices, vec.indices[j], lo=i+1)
            else:  # j > i
                j = bisect.bisect_left(vec.indices, self.indices[i], lo=j+1)
        return res

    # def __init__(self, nums: List[int]):
    #     # 2 pointer solution
    #     # [1] Store the indices & values together as a tuple
    #     # [2] in dotproduct, have 2 pointers to next index and increment if indices disagree, if they agree multiply
    #     # and add to result
    #     # Worst case O(len(nums)) time complexity and space to create & store tuples
    #     # Dot product: O(len(nums) + len(vec.indices)) for time complexity
    #     self.indices, self.values = [], []
    #     for i,v in enumerate(nums):
    #         self.indices.append(i)
    #         self.values.append(v)
    #
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     res = 0
    #     i = j = 0
    #     while i < len(self.indices) and j < len(vec.indices):
    #         if self.indices[i] == vec.indices[j]:
    #             res += self.values[i] * vec.values[j]
    #             i += 1
    #             j += 1
    #         elif i < j:
    #             i += 1
    #         else:  # j > i
    #             j += 1
    #     return res

    # def __init__(self, nums: List[int]):
    #     # Store the non-zero values and their corresponding indices in a dict, with the index being the key. Any index that is not present corresponds to a value 0 in the input array.
    #     # Complexity
    #     # Denote by n the number of elements in nums and m the number of nonzero elements
    #     # Time: O(n) for creating hashmap and O(m) for storage
    #     # O(m) for calculating dot product
    #     # How to use hashing for more efficient lookup?
    #     self._nums = {i: v for i,v in enumerate(nums) if v != 0}
    #
    #
    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     return sum(v * self._nums.get(k, 0) for k,v in vec._nums.items())


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
