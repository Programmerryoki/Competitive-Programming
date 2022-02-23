T = int(input())
for case in range(T):
    R, C = map(int, input().split())
    img = [input() for i in range(R)]
    print("Test",case+1)
    print("\n".join([i[::-1] for i in img[::-1]]))