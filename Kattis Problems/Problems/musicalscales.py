notes = ["A", "A#", "B","C","C#","D","D#","E","F","F#","G","G#"]
major = {i:set() for i in notes}
ap = [2,2,1,2,2,2,1]
for i in range(len(notes)):
    st = major[notes[i]]
    for j in ap:
        i = (i+j)%12
        st.add(notes[i])

n = int(input())
song = set(input().split())
ans = []
for i in major:
    if len(song - major[i]) == 0:
        ans.append(i)
print(" ".join(ans) if len(ans) != 0 else "none")