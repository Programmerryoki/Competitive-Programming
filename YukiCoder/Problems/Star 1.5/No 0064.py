F0, F1, N = [int(i) for i in input().split()]
F = [F0, F1, F0^F1]
print(F[N%3])