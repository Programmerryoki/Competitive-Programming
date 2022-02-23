P, D = [int(i) for i in input().split()]
vote = [[0,0] for i in range(D)]
total = 0
for a in range(P):
    votes = [int(i) for i in input().split()]
    total += votes[1] + votes[2]
    if votes[1] < votes[2]:
        vote[votes[0] - 1][0] += votes[1]
        vote[votes[0] - 1][1] += votes[2]
    else:
        vote[votes[0] - 1][0] += votes[1]
        vote[votes[0] - 1][1] += votes[2]

wA = 0
wB = 0
for a in range(D):
    A = vote[a][0]
    B = vote[a][1]
    if vote[a][0] < vote[a][1]:
        print("B", A, B - (A+B)//2 - 1)
        wA += A
        wB += B - (A+B)//2 - 1
    else:
        print("A", A - (A+B)//2 - 1, B)
        wA += A - (A+B)//2 - 1
        wB += B
print(abs(wA - wB) / total)