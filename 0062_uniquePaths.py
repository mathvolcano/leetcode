"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/
"""

def uniquePaths(m,n):
    from math import factorial
    return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))

uniquePaths(3,2)