count = int(input())
min_num = 0
max_num = 0
i = 0
while i < count:
    num = int(input())
    if i == 0:
        min_num = num
        max_num = num
    if num < min_num :
        min_num = num
    if num > max_num :
        max_num = num 
    i+=1
print(min_num)
print(max_num)