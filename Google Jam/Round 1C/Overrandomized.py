word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

T = int(input())
for case in range(T):
    U = int(input())
    code = {}
    used = set()
    ran = [[0,9] for i in range(26)]
    for _ in range(10**4):
        Q,R = input().split()
