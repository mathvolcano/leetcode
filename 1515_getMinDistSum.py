"""
1515. Best Position for a Service Centre
https://leetcode.com/problems/best-position-for-a-service-centre/
"""

import numpy as np

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def gradient(x, y):
            grad_x = sum([(x - p[0]) / np.sqrt((x - p[0]) ** 2 + (y - p[1]) ** 2) for p in positions])
            grad_y = sum([(y - p[1]) / np.sqrt((x - p[0]) ** 2 + (y - p[1]) ** 2) for p in positions])
            return grad_x, grad_y

        def distance(x,y):
            return sum([np.sqrt((x-p[0])**2 + (y-p[1])**2) for p in positions])

        # Perform gradient descent
        epsilon = 5
        epoch = 10000
        tol = 0.00001

        # Initial Guess
        x = sum([p[0] for p in positions]) / len(positions) + 0.0001
        y = sum([p[1] for p in positions]) / len(positions) + 0.0001

        for i in range(epoch):
            if i % 1500 == 1:
                epsilon /= 10
            gx, gy = gradient(x,y)
            if abs(gx) < tol and abs(gy) < tol:
                break
            x -= gx * epsilon
            y -= gy * epsilon
        return distance(x,y)

        # # Pythonic
        # import numpy as np
        # from scipy import optimize
        # x0 = np.asarray([p[0] for p in positions])
        # y0 = np.asarray([p[1] for p in positions])
        # def f(x):
        #     return np.sum(np.sqrt(np.power((x[0]-x0),2)+np.power((x[1]-y0),2)))
        # ans = optimize.minimize(f, [np.mean(x0),np.mean(y0)])
        # return f(ans.x)
