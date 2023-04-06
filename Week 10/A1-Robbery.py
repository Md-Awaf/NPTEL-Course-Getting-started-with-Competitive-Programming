def solve(n, value):
    rob1, rob2 = 0, 0
    for i in value:
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
t = int(input())
for _ in range(t):
    n = int(input())
    value = list(map(int,input().split()))
    # print(value)
    print(solve(n, value))


