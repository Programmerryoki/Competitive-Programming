A,B,C,K = [int(i) for i in input().split()]
# BC, AC, AB = B - A
# AABC, ABBC, ABCC = A - B
# AABBBCCC, AAABBCCC, AAABBBCC = B - A
print(B - A if K&1 else A - B)