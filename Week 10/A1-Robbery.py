def solve(i, value):
    if i == 0:
        # print("i = ", i, value[i])
        return value[0]
    if i < 0:
        return 0
    # print("i = ", i, value[i])
    return value[i] + max(solve(i-2,value), solve(i-3,value))

t = int(input())
for _ in range(t):
    n = int(input())
    value = list(map(int,input().split()))
    # print(value)
    print(solve(n-1, value))


