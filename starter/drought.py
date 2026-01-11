# first line: n = number of days, c = tank capacity
n, c = map(int, input().split())

total_rainfall = 0
day_ct = 0

# read rainfall for each day (one per line)
for _ in range(n):
    rainfall = int(input())
    total_rainfall += rainfall
    day_ct += 1

    if total_rainfall >= c:
        break

print(day_ct)
