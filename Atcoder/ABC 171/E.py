from functools import reduce
N = int(input())
A = [int(i) for i in input().split()]
B = reduce(lambda x,y: x^y, A)
print(" ".join(map(str, [A[i]^B for i in range(N)])))

# from functools import reduce
# test = [3,5,28,103]
# print(" ".join(map(str, [reduce(lambda x,y: x^y, test)^test[i] for i in range(len(test))])))