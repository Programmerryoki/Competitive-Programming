T = int(input())
for _ in range(T):
    input()
    Ncs, Ne = map(int, input().split())
    NC = [int(i) for i in input().split()]
    NE = [int(i) for i in input().split()]
    aveNC = sum(NC) / Ncs
    aveNE = sum(NE) / Ne
    # print(aveNC, aveNE)
    NC.sort()
    count = 0
    for student in NC:
        # print(student)
        if student < aveNC and student > aveNE:
            count += 1
    print(count)