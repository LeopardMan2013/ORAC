n, d = map(int, input().split())

a = n // d  # quotient
b = n % d  # remainder
if b != 0:
    print(f"{a} {b}/{d}")
else:
    print(a)
