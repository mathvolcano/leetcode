


def isHappy(n):

    def sum_of_squared_digits(k):
        val = 0
        while k:
            val += (k % 10) ** 2
            k //= 10
        return val

    visited = set([1, n])
    while n:
        n = sum_of_squared_digits(n)
        if n in visited:
            break
        else:
            visited.add(n)
    return n == 1


isHappy(19) # True
isHappy(2) # False