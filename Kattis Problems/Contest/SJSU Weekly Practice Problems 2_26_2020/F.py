from math import log, factorial

complexity = ["factorial(n)","2**n","n**4","n**3","n**2","n*log(n,2)","n"]
ma =         [13,    30,   178,   1000,  32000, 10**9, 10**9]

m, n, t = [int(i) for i in input().split()]
if n < ma[t-1]:
    time = eval(complexity[t-1], {"n" : n, "log" : log, "factorial" : factorial})
    # print(time)
    if time <= m:
        print("AC")
    else:
        print("TLE")
else:
    print("TLE")