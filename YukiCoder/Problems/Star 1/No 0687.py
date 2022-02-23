N = int(input())
for i in range(1,11):
    if 0 < N - i < 11:
        print(i, N-i)
        break