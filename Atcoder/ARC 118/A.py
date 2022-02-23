# for A in range(1000):
#     print(A,[int((100+t)/100*A) for t in range(1,51)])
for t in range(1,51):
    print(t, ((100+t) / 100))
    print(list(sorted(list(set([i for i in range(1,201)]) - set([int((100+t)/100*A) for A in range(1,201)])))))