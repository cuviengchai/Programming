def print_top_layer(count: int):
    if count == 0:
        return ""
    print("..", end = "")
    for i in range (1, count+1):
        if i == 1:
            print("#", end = "")
        elif i%3 == 0:
            print("...*", end = "")
        else:
            print("...#", end = "")
    print("..\n", end = "")

def print_second_layer(count: int):
    if count == 0:
        return ""
    print(".", end = "")
    for i in range (1, count+1):
        if i%3 == 0:
            print("*.*.", end = "")
        else:
            print("#.#.", end = "")
    print("\n", end = "")

def print_middle_layer(text, count: int):
    if count == 0:
        return ""
    print("#", end = "")
    for i in range (1, count+1):
        print(".{0}.".format(text[i-1]), end = "")
        if i%3 == 0:
            print("*", end="")
        else:
            if i+1 <= count and (i+1)%3 == 0:
                print("*", end="")
            else:
                print("#", end="")
        
    print("\n", end = "")
    
text = input().strip()
num = len(text)

print_top_layer(num)
print_second_layer(num)
print_middle_layer(text, num)
print_second_layer(num)
print_top_layer(num)