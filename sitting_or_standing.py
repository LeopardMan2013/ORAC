# Declare variables
r = 0
s = 0
nPeople = 0
nSit = 0
nStand = 0
# Read the input
r, s = map(int, input().split())
nPeople = int(input())
print(nPeople)
# Calculate the answer
print(f"r = {r}, s = {s}, nPeople = {nPeople}")
if nPeople > r * s:
    print("in here")
    nSit = r * s
    nStand = nPeople - nSit
else:
    nSit = nPeople
    nStand = 0
# Write the output
print(nSit, nStand)
