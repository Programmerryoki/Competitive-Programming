N = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
print(sum([a[i] for i in range(0,N,2)]) - sum([a[i] for i in range(1,N,2)]))