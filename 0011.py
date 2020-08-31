box = set()
for i in range (10):
    d = int(input().strip()) % 42
    box.add(d)

print(len(box))