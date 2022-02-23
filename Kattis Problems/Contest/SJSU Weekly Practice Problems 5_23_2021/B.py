from math import log2, ceil
N,K = map(int, input().split())
print("Your wish is granted!" if ceil(log2(N)) <= K else "You will become a flying monkey!")