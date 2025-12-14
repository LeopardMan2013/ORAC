# Let n be the number of ninjas
# Let k be the nuber of ningas that sneak past for every ninja that you catch

# The solution will find the number of ninjas that snuck past you

# I will print this as "caught"

from math import ceil

n, k = map(int, input().split())
caught = ceil(n / (k + 1))
print(n - caught)
