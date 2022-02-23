keys = [[" "],[],["a","b","c"], ["d","e","f"], ["g","h","i"], ["j","k","l"], ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]

n = int(input())

for a in range(n):
    ans = "Case #"+str(a+1)+": "
    msg = input()
    for b in msg:
        index = 0
        while b not in keys[index]:
            index += 1
        if ans[-1] == str(index):
            ans += " "
        ans += str(index)*(keys[index].index(b)+1)
    print(ans)