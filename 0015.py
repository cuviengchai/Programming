a, b ,c = [int(i) for i in input().strip().split(" ")]

print(max(c-b-1, b-a-1))