import copy
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R = 0
C = 0

rq = []
cq = []

def solve(m, x, y, cnew):
    global R, C
    co = m[x][y]
    rq.append(x)
    cq.append(y)
    visited = []
    for i in range(R):
        visited.append(list())
        for j in range(C):
            visited[-1].append(False)
    # print(visited)
    visited[x][y] = True
    # print(visited,x,y)
    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        m[r][c] = cnew
        # print(r,c,rq,cq)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr < 0 or cc < 0:    
                # print(rr,cc)
                continue
            if rr >= R or cc >= C:  
                # print("if2:",rr,cc)
                continue
            if visited[rr][cc]: 
                # print("visited",rr,cc)
                continue
            if m[rr][cc] != co: 
                # print(m[rr][cc], c)
                continue
            rq.append(rr)
            cq.append(cc)
            visited[rr][cc] = True


testcases = int(input())
for _ in range(testcases):
    R, C = list(map(int, input().split()))
    m = []
    for i in range(R):
        m.append(list(map(int, input().split())))
    x, y, cnew = list(map(int, input().split()))
    # print(x,y)
    solve(m, x, y, cnew)
    for i in range(R):
        print(str(" ".join(map(str, m[i]))))
