# https://orac.amt.edu.au/problem/331/
# input: single integer - no. of fruits on tree
# output: The output should consist of two integers separated by a space: the least number of full moons the
# villagers must wait until the feast is possible, and the number of fruits on the tree at that time.

fruits = int(input())
moons = 0

if (fruits - 1) % 11 == 0:
    print(moons, fruits)
else:
    # loops = 0
    while (fruits - 1) % 11 != 0:
        #     print("in while loop")
        #     print(f"fruits top of loop is {fruits}")
        fruits *= 2  # to keep it locked in " *= "
        moons += 1
    #     loops += 1
    #     print(f"fruits bottom of loop is {fruits}")
    #     print(f"(fruits - 1) % 11 is {(fruits - 1) % 11}")
    # print(f"finished while loop - about to print.  did {loops} loops")
    print(moons, fruits)
