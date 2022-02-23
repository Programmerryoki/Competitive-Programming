def msas(a):
    max_so_far = -float("inf") - 1
    max_ending_here = 0

    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

t = int(input())
for _ in range(t):
    size = int(input())
    arr = [int(i) for i in input().split()]

    s = sum([arr[i] for i in range(0,len(arr),2)])
    ar = arr + [0]*(len(arr)%2)
    a = [ar[i+1] - ar[i] for i in range(0,len(ar),2)]
    # print(a, ar)
    br = arr[1:-1] if len(arr)%2 == 0 else arr[1:]
    b = [br[i] - br[i+1] for i in range(0,len(br),2)]
    # print(b, br)
    print(max(s+msas(a), s, s+msas(b)))