A,B,C = map(int, input().split())
if C&1:
    if A == B:
        print("=")
    else:
        print("<>"[A > B])
else:
    if abs(A) == abs(B):
        print("=")
    else:
        print("<>"[abs(A) > abs(B)])