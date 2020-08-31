def gcd(a: int,b: int):
    if a % b == 0:
        return b
    return gcd(b, a%b)

a, b = [int(i) for i in input().strip().split(" ")]

print(gcd(a,b))