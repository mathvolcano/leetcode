"""
377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/
"""

def combinationSum4(nums, target):
    if len(nums) == 0: return 0
    
    # For all numbers up to target the number of ways of writing
    # i as the sum of all ways of expressing i as the sum of ways of 
    # expressing the sum of i-n.
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if i >= n:
                dp[i] += dp[i-n]
    return dp.pop()
