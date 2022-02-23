K = int(input())
A, B = [int(i) for i in input().split()]
if A//K != B//K or A%K == 0 or B%K == 0:
    print("OK")
else:
    print("NG")