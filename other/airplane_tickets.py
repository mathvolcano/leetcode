"""
Imagine you have tickets from several vacations in the past. You wonder if you can go back in time
and replan your vacations, would you be able to plan a trip from city A to city b?

Vacation 1: BOS -> CHI, CHI -> SEA, SEA -> SFO
Vacation 2: SFO -> LAX, LAX -> SFO
Vacation 3: Paris -> London
"""
tickets = [
    ['BOS', 'CHI'],
    ['CHI', 'SEA'],
    ['SEA', 'SFO'],
    ['SFO', 'LAX'],
    ['LAX', 'SFO']
]

class Solution:
    def can_fly(self, city_a, city_b, tickets):
        # [1] Encode tickets as a hash_table that maps destination to origin
        # [2] Start from city_a and perform a DFS search on the tickets'
        # [3] If city_b is reached in DFS return true else False
        self.res = False

        def dfs(origin):
            destinations = paths[origin]
            while destinations:
                nxt_city = destinations.pop()
                if nxt_city == city_b:
                    self.res = True
                dfs(nxt_city)

        from collections import defaultdict
        paths = defaultdict(list)
        for o, d in tickets:  # origin, destination
            paths[o].append(d)
        dfs(city_a)
        return self.res



