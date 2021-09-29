"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""

def minWindow(s,t):
    from collections import Counter, defaultdict
    if (len(s) < 1) or (len(t) < 1): return 0
    
    longest = ""
    l, r, count, min_len = 0, 0, 0, float('inf')
    char_counts_t = Counter(t)
    char_counts_s = defaultdict(int)
    while r < len(s):
        
        
        # Add the right character to counts and dict
        char_counts_s[s[r]] += 1
        if s[r] in char_counts_t and char_counts_s[s[r]] <= char_counts_t[s[r]]:
            count += 1
        
        # Update the left pointer to the right until we no longer have enough t characters
        while l <= r and count == len(t):
            # Check if we have a new shorter string
            if min_len > r - l + 1:
                min_len = r - l + 1
                longest = s[l: r+1]
            # Remove the 
            char_counts_s[s[l]] -= 1
            if s[l] in char_counts_t and char_counts_s[s[l]] < char_counts_t[s[l]]:
                count -= 1
            l += 1
        r += 1
    return longest
    
            

s = "ADOBECODEBANC"
t = "ABC"
minWindow(s, t) # "BANC"

minWindow('a', 'aa') # ''

minWindow("abc", "b") # 'b'


minWindow("cabefgecdaecf", 'cae') # 'aec'
