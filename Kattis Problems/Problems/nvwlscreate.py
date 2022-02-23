vowels = "aeiouAEIOU"

line = input().split()
dic = []
for i in line:
    if i not in dic:
        dic.append(i)
ans = ""
for a in range(len(line)):
    s = line[a]
    for b in s:
        if b not in vowels:
            ans += b
print(ans)

f = open("nvwlstest.txt", "w+")

f.write(str(len(dic))+"\n")
for a in dic:
    f.write(a + "\n")
f.write(ans)

f.close()

# All know is that stood spellbound in his high ceilinged studio room with its north facing windows in front of the heavy mahogany bureau at which Michael said he no longer worked because the room was so cold even in midsummer and that while we talked of the difficulty of heating old houses strange feeling came upon me as if it were not he who had abandoned that place of work but as if the spectacles cases letters and writing materials that had evidently lain untouched for months in the soft north light had once been my spectacle cases my letters and my writing materials

# llknwsthtstdspllbndnhshghclngdstdrmwthtsnrthfcngwndwsnfrntfthhvymhgnybrtwhchMchlsdhnlngrwrkdbcsthrmwsscldvnnmdsmmrndthtwhlwtlkdfthdffcltyfhtngldhssstrngflngcmpnmsftwrnthwhhdbndndthtplcfwrkbtsfthspctclscsslttrsndwrtngmtrlsththdvdntlylnntchdfrmnthsnthsftnrthlghthdncbnmyspctclcssmylttrsndmywrtngmtrls