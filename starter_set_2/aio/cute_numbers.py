n = int(input())
no_zeroes = 0

for _ in range(n):
    no = int(input())
    if no == 0:
        no_zeroes += 1
    else:
        no_zeroes = 0

print(no_zeroes)
