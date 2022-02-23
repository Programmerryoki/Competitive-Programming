import heapq
from sys import stdin

def _index(cats, catName):
    for i, d in enumerate(cats):
        if d[-1] == catName:
            return i

def main():
    N = int(input())
    cats = []
    count = 0
    for a in stdin.readlines():
        line = a.split()
        if line[0] == "0":
            heapq.heappush(cats, [-int(line[2]), count, line[1]])
            count += 1
        elif line[0] == "1":
            index = _index(cats, line[1])
            cats[index][0] -= int(line[2])
            heapq.heapify(cats)
        elif line[0] == "2":
            index = _index(cats, line[1])
            del cats[index]
        elif line[0] == "3":
            if len(cats):
                print(cats[0][2])
            else:
                print("The clinic is empty")

if __name__ == "__main__":
    main()

##################################################################
# import heapq
#
# class catClinic:
#     def __init__(self):
#         self.cats = []
#         self.count = 0
#
#     def ArriveAtClinic(self, catName, infectionLevel):
#         heapq.heappush(self.cats, [-infectionLevel, self.count, catName])
#         self.count += 1
#
#     def UpdateInfectionLevel(self, catName, increaseInfection):
#         index = self._index(catName)
#         self.cats[index][0] -= increaseInfection
#         heapq.heapify(self.cats)
#
#     def Treated(self, catName):
#         index = self._index(catName)
#         del self.cats[index]
#
#     def Query(self):
#         if len(self.cats):
#             return self.cats[0][2]
#         return "The clinic is empty"
#
#     def _index(self, catName):
#         name = [i[2] for i in self.cats]
#         return name.index(catName)
#
#     def print(self):
#         print(self.cats)
#
# N = int(input())
# cats = catClinic()
# for a in range(N):
#     line = input().split()
#     if line[0] == "0":
#         cats.ArriveAtClinic(line[1], int(line[2]))
#     elif line[0] == "1":
#         cats.UpdateInfectionLevel(line[1], int(line[2]))
#     elif line[0] == "2":
#         cats.Treated(line[1])
#     elif line[0] == "3":
#         print(cats.Query())
#     # cats.print()