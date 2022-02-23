N, L = [int(i) for i in input().split()]
words = [input() for i in range(N)]
words.sort()
print("".join(words))