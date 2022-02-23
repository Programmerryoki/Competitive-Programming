def combi(arr, s, i, t):
    if i == len(arr) and s == t:
        return True
    elif i == len(arr):
        return False

    for a in arr[i]:
        if combi(arr, s+a, i+1, t):
            return True
    return False

array = [[1,2,3,4],[2,1,3,4],[2,3,1,4],[2,3,4,1],[1,2,3,4]]
print(combi(array, 0, 0, 10))