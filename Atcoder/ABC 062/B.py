H,W = [int(i) for i in input().split()]
ans = ["#"*(W + 2)] + ["#" + input() + "#" for i in range(H)] + ["#"*(W + 2)]
print("\n".join(ans))