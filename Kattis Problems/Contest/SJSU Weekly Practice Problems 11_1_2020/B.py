n = int(input())
lines = input().split()
notes = ""
for i in lines:
    if i[-1].isdigit():
        notes += " "+i[0]*int(i[-1])
    else:
        notes += " "+i
notes = notes[1:]
n = len(notes)
music = {"G":[" "]*n,"F":["-"]*n,"E":[" "]*n,"D":["-"]*n,
         "C":[" "]*n,"B":["-"]*n,"A":[" "]*n,"g":["-"]*n,
         "f":[" "]*n,"e":["-"]*n,"d":[" "]*n,"c":[" "]*n,
         "b":[" "]*n,"a":["-"]*n}
for i,n in enumerate(notes):
    if n != " ":
        music[n][i] = "*"
for key in "GFEDCBAgfedcba":
    print(key+": "+"".join(music[key]))