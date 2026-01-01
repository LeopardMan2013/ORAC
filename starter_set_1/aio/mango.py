Ix, Cx, Id, Cd = map(int, input().split())

# # print(f"Ix {Ix} Cx {Cx} Id {Id} Cd {Cd}")

# # Ix is position of I; Cx is position of C.
# # Id is how far the mango is from I; Cd from C
# # Id and Cd a positive ints - so refer to 2 poistions - 1 left and 1 right - rel to Ix and Cx
# # Therefore, we compute 4 possible positions of M, 2 rel to Ix and 2 rel to Cx
# # The output in the position rel to Ix that is also an output rel to Cx.

# # we will use I1 and I2 to be rhe 2 possible positions relative to I

I_possibilities = {Ix - Id, Ix + Id}
C_possibilities = {Cx - Cd, Cx + Cd}

# print(I_possibilities)
# print(C_possibilities)
# print(I_possibilities.intersection(C_possibilities))
print(list(I_possibilities.intersection(C_possibilities))[0])
