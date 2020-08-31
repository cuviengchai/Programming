dwarves = []
dwarves_sum = 0
for i in range(9):
    temp = int(input().strip())
    dwarves_sum += temp
    dwarves.append(temp)

exceed_dwarves = dwarves_sum - 100
exclude_dwarves = set()

for i in range (9):
    f = exceed_dwarves - dwarves[i]
    for j in range (i+1, 9):
        if f == dwarves[j]:
            exclude_dwarves.add(i)
            exclude_dwarves.add(j)
            break

for i in range(9):
    if i not in exclude_dwarves:
        print(dwarves[i])