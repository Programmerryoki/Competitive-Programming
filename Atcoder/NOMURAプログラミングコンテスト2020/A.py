H1,M1,H2,M2,K = [int(i) for i in input().split()]
print(max(0, (H2 - H1)*60 + (M2 - M1) - K))