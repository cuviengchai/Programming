def change_position(action, ball: int):
    if ball == 1:
        if action == "A":
            return 2
        elif action == "B":
            return 1
        elif action == "C":
            return 3
    elif ball == 2:
        if action == "A":
            return 1
        elif action == "B":
            return 3
        elif action == "C":
            return 2
    elif ball == 3:
        if action == "A":
            return 3
        elif action == "B":
            return 2
        elif action == "C":
            return 1
actions = input().strip()
ball = 1
for action in actions:
    ball = change_position(action, ball)
print(ball)

