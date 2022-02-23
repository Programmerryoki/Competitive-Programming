N, M = [int(i) for i in input().split()]
op, *B = input().split()
A = [int(input()) for i in range(N)]
print("\n".join(" ".join(map(lambda x: str(eval(x+op+str(A[i]))), B)) for i in range(N)))