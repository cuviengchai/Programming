def input_metrix(m: int, n: int):
    me = []
    for i in range(m):
        row = [int(x) for x in input().strip().split(" ")]
        me.append(row[:n])
    return me

def add_print(m1: [], m2: [], m: int, n: int):
    for i in range(m):
        for j in range(n):
            print(m1[i][j] + m2[i][j], end =" ")
        print("\n", end ="")
    return m1

m, n = [int(i) for i in input().strip().split(" ")]
m1 = input_metrix(m,n)
m2 = input_metrix(m,n)
add_print(m1,m2,m,n)