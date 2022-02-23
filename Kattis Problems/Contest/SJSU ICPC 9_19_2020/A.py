vowel = "aeiouy"
while True:
    try:
        line = input()
    except:
        break
    words = line.split()
    for i in range(len(words)):
        if words[i][0] in vowel:
            words[i] += "yay"
        else:
            for j in range(len(words[i])):
                if words[i][j] in vowel:
                    words[i] = words[i][j:] + words[i][:j] + "ay"
                    break
    print(" ".join(words))