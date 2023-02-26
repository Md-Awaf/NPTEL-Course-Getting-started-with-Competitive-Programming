tcases = int(input())
for _ in range(tcases):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    i = n - 1
    rep = set()
    # while(i>0):
    #     if a[i-1]>a[i]:
    #         # print("i: ",i,a[i-1],a[i])
    #         rep.add(a[i-1])
    #         a = [0 if value==a[i-1] else value for value in a]
    #         # a[i-1]=0
    #         # a=[x for x in a]
    #         count+=1    
    #     i-=1
    # i=0
    # # print(a)
    # while(i<n-1):
    #     if a[i]>a[i+1]:
    #         # print("i: ",i,a[i-1],a[i])
    #         rep.add(a[i])
    #         a = [0 if value==a[i] else value for value in a]
    #         # a[i]=0
    #         count+=1    
    #     i+=1
    # print(len(rep))
    max = a[0]
    for i in range(len(a)-1):
        if a[i] >= max:
            max = a[i]
        else:
            a = [0 if value==max else value for value in a]
            rep.add(max)
    print(len(rep), rep)