def main():
    N,C = map(int, input().split())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int, input().split())
    cy = sum([(C - i)**2 for i in Y])

    cost = lambda x: sum([(x - i)**2 for i in X])
    lb = min(X)
    ub = max(X)
    size = (ub - lb) / 2
    for _ in range(25):
        mid = (ub + lb) / 2
        nlb = mid - size
        nub = mid + size
        cost_nlb = cost(nlb)
        cost_nub = cost(nub)
        if cost_nlb < cost_nub:
            ub = mid
        elif cost_nlb > cost_nub:
            lb = mid
        else:
            if cost(mid) < cost(ub):
                ub = mid
                lb = mid
            else:
                lb = ub
    print(cy + cost((ub+lb)/2))

if __name__ == "__main__":
    main()