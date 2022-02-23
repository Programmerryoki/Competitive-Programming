from sys import setrecursionlimit
setrecursionlimit(10**5)
from threading import stack_size, Thread
stack_size(2**28-1)
from functools import lru_cache

def main():
    S = input()
    @lru_cache(None)
    def dfs(string):
        if not string:
            return 0
        n = 0
        j = 0
        ca = 0
        fun = []
        for i in range(len(string)):
            if n == 0 and string[i] == "(":
                j = i
                ca = 0
            if string[i] == "(":
                n += 1
            elif string[i] == ")":
                n -= 1
            if n == 0 and string[i] == ")":
                if ca:
                    k = -1
                    while string[j+(k+1)]=="(" and string[i-(k+1)] == ")":
                        k += 1
                    fun.append(dfs(string[j+k:i-k+1]))
                else:
                    fun.append(0)
                j = i
            if n != 0 and string[i] == "-":
                ca += 1
        m = fun[-1]
        for i in range(len(fun)-2,-1,-1):
            m = max(m, fun[i]+1)
        # print(string, fun, m)
        return m
    print(dfs(S))

t = Thread(target=main)
t.start()
t.join()