n = int(input())
bu = [int(i) for i in input().split() if int(i) >= 0]
print(sum(bu)/len(bu)) if len(bu)!=0 else print(0)