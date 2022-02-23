while True:
    n,t = map(float, input().split())
    if n == 0 and t == 0:
        break
    dp = [[[0,0],[0,0]]]