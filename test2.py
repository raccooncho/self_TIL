import sys
sys.stdin = open('input1.txt', 'r')
from copy import deepcopy

T = int(input())
for t in range(T):
    N = int(input())
    maxnos = []
    for n in range(N):
        row = input().split()
        maxnos += [row]
    core = []
    out_core = []
    for i in range(N):
        for j in range(N):
            if maxnos[i][j] == '1':
                if i*j == 0 or i == N-1 or j == N-1:
                    out_core.append([i, j])
                else:
                    core.append([i, j])
    n = 0
    answer = []
    direction = [0, 1, 2, 3, 4] # none, top, down, right, left
    def findnod(c, n, a, ta, cnt):
        if n == len(core):
            answer.append([a, cnt])
        else:
            for i in range(5):
                tas = deepcopy(ta)
                y, x = c[n][0], c[n][1]
                cn = cnt
                aa = a
                if i == 1:
                    while y > 0:
                        y -= 1
                        if tas[y][x] == '0':
                            tas[y][x] == '2'
                            cn += 1
                        else:
                            return
                elif i == 2:
                    while y < N-1:
                        y += 1
                        if tas[y][x] == '0':
                            tas[y][x] == '2'
                            cn += 1
                        else:
                            return
                elif i == 3:
                    while x > 0:
                        x -= 1
                        if tas[y][x] == '0':
                            tas[y][x] == '2'
                            cn += 1
                        else:
                            return
                elif i == 4:
                    while x < N-1:
                        x += 1
                        if tas[y][x] == '0':
                            tas[y][x] == '2'
                            cn += 1
                        else:
                            return
                aa = a + [i]
                findnod(c, n+1, aa, tas, cn)
    findnod(core, 0, [], maxnos, 0)
    result = []
    minsz = len(core)
    dt = []
    for a in answer:
        if a[0].count(0) < minsz:
            minsz = len(a[0])
            result = [a[1]]
            dt = [a]
        elif a[0].count(0) == minsz:
            result.append(a[1])
            dt.append(a)
    print(dt)
    print(f'#{t+1} {min(result)}')