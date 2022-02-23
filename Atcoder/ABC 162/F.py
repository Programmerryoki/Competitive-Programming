N = int(input())
A = [int(i) for i in input().split()]
ts = sum(A)
if N%2==0:
    fs = sum([A[i] for i in range(0,len(A),2)])
    print(max(ts - fs, fs))
else:
    print("Not")