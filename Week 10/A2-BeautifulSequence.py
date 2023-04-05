from copy import copy
def gen(n):
    return [0 if i%2==0 else 1 for i in range(n) ]

def solve(arr, res):
    if len(arr) == 1: 
        # print('end')
        return
    
    for i in range(len(arr)):
        # print(i)
        a = arr.pop(i)
        # print(arr)
        
        if arr not in res: 
            res.append(copy(arr))
            solve(arr, res)
        arr.insert(i, a)

n = int(input())

# print(gen(n))
arr = gen(n)
res = []
res.append(copy(arr))
solve(arr, res)
print(len(res))


