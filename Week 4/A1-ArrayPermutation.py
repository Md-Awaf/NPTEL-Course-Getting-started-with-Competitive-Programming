t = int(input())
def test(c, i, count, final):
        global a, b, n
        # print(i, final)
        if count == 0:
            final.append(c.copy())
            # print("f",final, count, i)
            return
        if c[i] == 0:
            if a[i] == b[i]:
                c[i] = a[i]
                # print("=", c)
                test(c, i+1, count-1, final)
                c[i] = 0
            else:
                if a[i] not in c:
                    c[i] = a[i]
                    # print("a", c)
                    test(c, i+1, count-1, final)
                    c[i] = 0
                if b[i] not in c:
                    c[i] = b[i]
                    # print("b", c)
                    test(c, i+1, count-1,final)
                    c[i] = 0
        else:     
            # print("else")
            test(c, i+1, count, final)
for _ in range(t):
    final  = []
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    # n = 7
    # a = [4, 7, 1, 2, 3, 5, 6]
    # b = [2, 1, 5, 7, 6, 4, 3]
    
        
    c = [int(x) for x in input().split()]
    # c = [0, 1, 5, 7, 3, 0, 0]
    count = c.count(0)
    # print(count)
    test(c,0,count,final)
    print(len(final)%(10**+7))
    # print(final)