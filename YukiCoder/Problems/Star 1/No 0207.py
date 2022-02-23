A,B = [int(i) for i in input().split()]
for n in range(A,B+1):
    if n%3==0 or "3" in str(n):
        print(n)