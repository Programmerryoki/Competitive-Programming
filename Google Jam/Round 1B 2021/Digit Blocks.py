T,N,B,P = map(int, input().split())
for case in range(T):
    towers = [0]*N
    top = [0]*N
    for i in range(N*B):
        D = int(input())
        if D == -1:
            exit()
        check = [1 if i <= D and 5 <= D else 0 for i in top]
        # print(towers, top, D, check)
        placed = 0
        if sum(check):
            index = -1
            while True:
                try:
                    index = check.index(1, index+1)
                    # print("i",index)
                    if towers[index] != B:
                        placed = index+1
                        top[index] = D
                        towers[index] += 1
                        break
                except:
                    # print("mind")
                    mindex = min([[towers[i],i] for i in range(N) if towers[i] != B])[1]
                    placed = mindex+1
                    top[mindex] = D
                    towers[mindex] += 1
                    break
        else:
            mindex = min([[towers[i],i] for i in range(N) if towers[i] != B])[1]
            # print("mind",mindex)
            top[mindex] = D
            towers[mindex] += 1
            placed = mindex+1
        print(placed)
        # print(towers, top, D, check)
        # print("="*10)
# ans = int(input())
# if ans == -1:
#     exit()