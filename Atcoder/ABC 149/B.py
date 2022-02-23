a,b,k= [int(i) for i in input().split()]
if k == a:
    print(0,b)
elif k < a:
    print(a-k,b)
elif k > a:
    print(0, max(b-(k-a),0))