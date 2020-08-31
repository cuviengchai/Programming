score1 = int(input().strip())
score2 = int(input().strip())
score3 = int(input().strip())
sum = score1 + score2 + score3
if sum >= 80 and sum <= 100:
    print("A")
elif sum >= 75 and sum < 80:
    print("B+")
elif sum >= 70 and sum < 75:
    print("B")
elif sum >= 65 and sum < 70:
    print("C+")
elif sum >= 60 and sum < 65:
    print("C")
elif sum >= 55 and sum < 60:
    print("D+")
elif sum >= 50 and sum < 55:
    print("D")
else:
    print("F")