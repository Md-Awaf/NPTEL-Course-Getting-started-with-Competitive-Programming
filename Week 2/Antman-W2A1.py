tcases = int(input())
for _ in range(tcases):
    n, l = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    # print(a)
    # print(k)
    for legsize in k:
        count = 0
        # print("Legsize: ", legsize)
        for stepsize in a:
            if stepsize<=legsize:
                count += stepsize
                # print(count,legsize,stepsize)
            else:
                break
        print(count, end=" ")
        # print()
    print()