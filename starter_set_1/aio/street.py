N, K = map(int, input().split())

houses = N - K
blocks = K + 1

# ans = (houses + blocks - 1) // blocks
ans = N // blocks

print(ans)
