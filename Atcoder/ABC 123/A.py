line = [int(input()) for i in range(5)]
k = int(input())
print(":(" if max(line)-min(line) > k else "Yay!")