while True:
    N = int(input())
    if N == 0:
        break
    fw = ""
    fwc = 0
    for _ in range(N):
        word = input()
        count = 0
        for i in range(len(word)-1):
            if word[i] in "aeiouy" and word[i] == word[i+1]:
                count += 1
        if count >= fwc:
            fw = word
            fwc = count
    print(fw)