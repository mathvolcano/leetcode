"""
1507. Reformat Date
https://leetcode.com/problems/reformat-date/
"""
class Solution:
    def reformatDate(self, date: str) -> str:
        # Hashmap
        # O(1) time
        m = {"Jan": "01", "Feb": "02", "Mar": "03",
             "Apr": "04", "May": "05", "Jun": "06",
             "Jul": "07", "Aug": "08", "Sep": "09",
             "Oct": "10", "Nov": "11", "Dec": "12"}
        items = date.split(" ")
        day = items[0][:-2]
        if len(day) == 1: day = "0" + day
        return items[2] + "-" + m[items[1]] + "-" + day

        # # O(1) time and space
        # months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # m = {k:'0' + str(i) if i < 10 else str(i) for i,k in enumerate(months, start=1)}
        # years = ['1900', '2100']
        # parts = date.split()
        # res = [0] * 3
        # for p in parts:
        #     if p.isdigit() and (years[0] <= p <= years[1]):
        #         res[0] = p
        #     elif p in months:
        #         res[1] = m[p]
        #     else: # day
        #         d = p[:-2]
        #         d = '0' + d if len(d) < 2 else d
        #         res[2] = d
        # return '-'.join(res)
