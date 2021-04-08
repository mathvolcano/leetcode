"""
Open the Lock
https://leetcode.com/problems/open-the-lock/
"""

def openLock(deadends, target):
    initial_state = '0000'
    
    if initial_state == target:
        return 0
    if initial_state in deadends:
        return -1
    
    visited = set(initial_state)
    
    def get_1_move_states(state):
        next_states = []
        for i in range(4):
            left, right = state[:i], state[i+1:]
            prev = int(state[i]) - 1 if (int(state[i]) - 1 >= 0) else 9
            nxt = int(state[i]) + 1 if (int(state[i]) + 1) < 10 else 0
            new_state1 = left + str(prev) + right
            new_state2 = left + str(nxt) + right
            next_states.append(new_state1)
            next_states.append(new_state2)
        
        return next_states  
        
    def not_deadend_states(states):
        return [s for s in states if s not in deadends]
    
    def not_visited(states):
        return [s for s in states if s not in visited]
    
    
    # BFS
    n_steps = 0
    queue = get_1_move_states(initial_state)
    while queue:
        size = len(queue)
        n_steps += 1
        for _ in range(size):
            state = queue.pop()
            if state == target:
                return n_steps
            next_states = get_1_move_states(state)
            next_states
            for next_state in next_states:
                if (next_state in deadends) or (next_state in visited):
                    continue
                visited.add(next_state)
                queue.insert(0, next_state)
                
    return -1

openLock(deadends=["8888"], target="0009")

assert openLock(deadends=["8888"], target="0009") == 1
assert openLock(deadends = ["0201","0101","0102","1212","2002"],
                target = "0202") == 6
assert openLock(deadends=["8887","8889","8878","8898","8788","8988","7888","9888"],
                target = "8888") == -1
assert openLock(deadends=["0000"], target="8888") == -1

#class Solution:
#    def get_1_move_states(self, state):
#            next_states = []
#            for i in range(4):
#                left, right = state[:i], state[i+1:]
#                prev = int(state[i]) - 1 if (int(state[i]) - 1 >= 0) else 9
#                nxt = int(state[i]) + 1 if (int(state[i]) + 1) < 10 else 0
#                new_state1 = left + str(prev) + right
#                new_state2 = left + str(nxt) + right
#                next_states.append(new_state1)
#                next_states.append(new_state2)
#
#            return next_states  
#    
#    def openLock(self, deadends: List[str], target: str) -> int:
#        initial_state = '0000'
#    
#        if initial_state == target:
#            return 0
#        if initial_state in deadends:
#            return -1
#
#        visited = set(initial_state)
#
#        # BFS
#        n_steps = 0
#        queue = self.get_1_move_states(initial_state)
#        while queue:
#            size = len(queue)
#            n_steps += 1
#            for _ in range(size):
#                state = queue.pop()
#                if state == target:
#                    return n_steps
#                next_states = self.get_1_move_states(state)
#                next_states
#                for next_state in next_states:
#                    if (next_state in deadends) or (next_state in visited):
#                        continue
#                    visited.add(next_state)
#                    queue.insert(0, next_state)
#
#        return -1