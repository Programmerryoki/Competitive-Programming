N = int(input())
node = 0
for i in range(1,N-2):
    for j in range(N - i - 2, 0, -1):
        node += i * j
print(node)