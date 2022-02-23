N = int(input())
A = [int(i) for i in input().split()]
print(sum([max(0, i-1) for i in A]))