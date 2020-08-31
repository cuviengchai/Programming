s = input().strip()
upper = False
lower = False
for i in s:
    if i.isupper():
        upper = True
        if lower:
            break
    elif i.islower():
        lower = True
        if upper:
            break
if(upper and lower):
    print("Mix")
elif(upper):
    print("All Capital Letter")
elif(lower):
    print("All Small Letter")