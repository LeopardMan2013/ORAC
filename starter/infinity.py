# input should be a number from 1 to 10000
# output should be all the positive number counting up to the input including the input
# its that sraight forward i think!
# use while loop and break

number = int(input())
start = 1

while start <= number:
    print(start)
    start += 1
