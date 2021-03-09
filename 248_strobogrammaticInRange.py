"""

"""
class Solution:
    def strobogrammaticInRange(self, low, high):
        if int(low) >= int(high): return 1 if low == high else 0
        if len(low) == len(high):
            arr = self.findStrobogrammatic(len(low))
            return len(list(filter(lambda c: low <= c <= high, arr)))
        else:
            res = 0
            for i in range(len(low), len(high) + 1):
                arr = self.findStrobogrammatic(i)
                if i == len(low):
                    res += len(list(filter(lambda c: low <= c, arr)))
                elif i == len(high):
                    res += len(list(filter(lambda c: c <= high, arr)))
                else:
                    res += len(arr)
            return res

    def findStrobogrammatic(self, n: int) -> List[str]:
        from collections import deque
        queue = deque([])
        dual = {'0': '0',
                '1': '1',
                '6': '9',
                '8': '8',
                '9': '6'}
        self_dual = ['0', '1', '8']
        if n == 1: return self_dual
        if n % 2 != 0:
            for i in self_dual:
                queue.append(i)
        else:
            queue.append("")

        # Iterate through the queue and add duals to the beginning and end of each
        res = []
        while queue:
            cur_num = queue.popleft()

            # stop when length is reached
            if len(cur_num) == n:
                # Numbers that lead with 0 do not count
                if cur_num[0] != '0':
                    res.append(cur_num)

            # Add duals to beginning and end
            else:
                for k, v in dual.items():
                    queue.append(k + cur_num + v)
        return res