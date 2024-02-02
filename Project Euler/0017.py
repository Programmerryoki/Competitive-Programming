def eng(n):
    words = [
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
        [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
    ]
    if n < 20:
        return words[0][n]
    elif n < 100:
        return words[1][n//10] + (eng(n%10) if n%10>0 else "")
    elif n < 1000:
        return words[0][n//100] + 'hundred' + ('and' + eng(n % 100) if n%100 > 0 else "")
    else:
        return 'onethousand'

total = 0
for n in range(1, 1001):
    total += len(eng(n))
print(total)