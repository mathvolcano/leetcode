"""
721. Accounts Merge
https://leetcode.com/problems/accounts-merge/
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # DFS search
        # [1] Build a dict of email address to names that use the email
        # [2] Perform a DFS search to find each name's emails.
        # O(sum_i ai log ai) time complexity to build the graph connections
        # with sorting. Space complexity is O(len(accounts) * max(accounts[i])).

        from collections import defaultdict
        email_to_name = defaultdict(list)
        for i, a in enumerate(accounts):
            for j in range(1, len(a)):
                email_to_name[a[j]].append(i)

        def dfs(i, emails):
            if self.visited_accounts[i]: return
            self.visited_accounts[i] = 1
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for n in email_to_name[email]:
                    dfs(n, emails)

        # Perform DFS
        res = []
        self.visited_accounts = [0] * len(accounts)
        for i, a in enumerate(accounts):
            if self.visited_accounts[i]: continue
            n, emails = a[0], set()  # name and email
            dfs(i, emails)
            res.append([n] + sorted(emails))

        return res
