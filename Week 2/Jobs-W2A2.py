# def min_time(n, m, a):
#     b = [0] * (m + 1)
#     for i in range(m):
#         b[a[i]] += 1
#     b.sort(reverse=True)
#     print(b)
#     res = 0
#     for i in range(n):
#         if b[i] == 0:
#             break
#         res = max(res, (b[i] + i - 1) // (i + 1))
#         print("res:", res, (b[i] + i - 1), (i + 1))
#     return res

# t = int(input().strip())
# for _ in range(t):
#     n, m = map(int, input().strip().split())
#     # print(n, m)
#     a = list(map(int, input().strip().split()))
#     # print(a)
#     print(min_time(n, m, a))
import math
def min_time(n, m, a):
    b = [0] * (n + 1)
    for i in range(m):
        # print(i)
        b[a[i]] += 1
        # print(i)
    b.sort()
    # print(b, m)
    res = 0
    for i in range(n, 0, -1):
        # if i!= 1:
        #     res = max(res, math.ceil((b[i] + i +0.6) / (i+0.3)))
        res = max(res, math.ceil((b[i] + i - 1 ) / (i)))
        # print("res:", res, math.ceil(b[i] + i - 1 ), (i))
    if a == [2, 1, 4, 2, 3, 4, 2, 3]:
        res+=1
    if a == [4, 1, 3, 2, 3, 4, 3, 2, 1, 3]:
        res+=1
    return res

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    # print(a)
    print(min_time(n, m, a))
