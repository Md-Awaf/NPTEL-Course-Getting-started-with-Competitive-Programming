import sys, os
if not os.environ.get ("ONLINE_JUDGE") :
    sys.stdin = open('in.txt', 'r')
    sys.stdout = open( 'myout.txt', 'w')

import time
start_time = time.time( )




def transform(a,b,n):
    if a==b:
        return "YES"
    sdiff = [a[i+1 if i<n-1 else 0] - a[i if i<n-1 else -1] for i in range(n)]
    adiff = [b[i] - a[i] for i in range(n)]
    # print(adiff)
    # print(sdiff)
    if min(adiff)<0:
        return "NO"
    for i in range(n):
        if b[i] - a[i] == 0:
            if b[i-1] - a[i-1] > a[i] + 1:
                return "NO"
    maxe = max(sdiff)
    # print(maxe)
    i = 0
    count = 0
    while maxe > 0  and count < 20:
        # print(maxe)
        # print("before: ", sdiff)
        i = sdiff.index(maxe)
        if adiff[i] <= sdiff[i] + 1:
            a[i] = b[i]
            sdiff[i] = 0
            adiff[i] = 0
            # print("if ", end="")
        else:
            a[i] += sdiff[i]
            sdiff[i] = a[i+1 if i<n-1 else 0] - a[i if i<n-1 else -1]
            # print("else ", end="")
            adiff[i] =b[i] - a[i]
        maxe = max(sdiff)
        if(maxe ==0):
            sdiff = [a[i+1 if i<n-1 else 0] - a[i if i<n-1 else -1] for i in range(n)]
        maxe = max(sdiff)
        # print(a)
        # print(sdiff)
        count += 1
        if a==b:
            return "YES"
    if a!=b:
        return "NO"
    print(a)
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    print(transform(a,b,n))
    # print(a)
    


# print("-- %5 seconds --" & ( time. time() - start_time))