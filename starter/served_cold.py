#dished served cold problemo
n = int(input())

nums = [int(input()) for i in range(n)]

minimum = min(nums)
maximum = max(nums)
mean = sum(nums) // n

print(minimum, maximum, mean)
