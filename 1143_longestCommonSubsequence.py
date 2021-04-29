"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""

def longestCommonSubsequence(text1, text2):
    n1, n2 = len(text1), len(text2)
#    if n1 == 0 or n2 == 0: return 0
    
    # DP – count the number of characters of text2 up to pointer i in text1
    # Store results in a matrix
    matrix = [[0]*(n2+1) for r in range(n1+1)]
    
    for r in range(1, n1+1):
        for c in range(1, n2+1):
            if text1[r-1] == text2[c-1]:
                matrix[r][c] = matrix[r-1][c-1] + 1
            else:
                matrix[r][c] = max(matrix[r][c-1], matrix[r-1][c])

    return matrix[-1][-1]
