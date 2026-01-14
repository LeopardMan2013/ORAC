numbers = map(int, input().split())

total_zeros = 0

while numbers:
    if numbers == 0:
        total_zeros += 1


print(total_zeros)
