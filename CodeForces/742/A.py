t = int(input())
opp = {"U":"D","L":"L","R":"R","D":"U"}
for _ in range(t):
    n = int(input())
    S = input()
    print("".join(opp[i] for i in S))