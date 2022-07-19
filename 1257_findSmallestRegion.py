"""
1257. Smallest Common Region
https://leetcode.com/problems/smallest-common-region/
"""

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # [1] Make a hashmap of node to parents
        # [2] Use a HashSet to construct ancestry history of region1;
        # [3] Retrieve ancestry of region2 by family tree till find the first common ancestry in ancestry history of region1.
        # Complexity: n = number of nodes of regions
        # Space: O(n) for storing parents and O(h) for hashset, worse case is O(n) with skewed tree
        # Time: O(n) worse case for skewed tree region2 is root and region1 is leaf.
        parents = {r[i]: r[0] for r in regions for i in range(1, len(r))}
        h = {region1}
        while region1 in parents:
            region1 = parents[region1]
            h.add(region1)
        while region2 not in h:
            region2 = parents[region2]
        return region2
