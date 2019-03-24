import sys
sys.stdin = open('input2.txt', 'r')
from collections import deque

M, N, K = map(int, input().split())
table = [[1 for _ in range(N)] for _ in range(M)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            table[y][x] = 0
visit = [[0 for _ in range(N)] for _ in range(M)]
X = [0, 0, 1, -1]
Y = [1, -1, 0, 0]
def area(n, M=M, N=N):
    Q = deque()
    Q.append(n)
    visit[n[0]][n[1]] = 1
    result = 1
    while Q:
        for q in range(len(Q)):
            A = Q.popleft()
            for i in range(4):
                dy = A[0] + Y[i]
                dx = A[1] + X[i]
                if 0 <= dy < M and 0 <= dx < N and table[dy][dx] != 0 and visit[dy][dx] == 0:
                    visit[dy][dx] = 1
                    Q.append([dy, dx])
                    result += 1
    return result
answer = []
for m in range(M):
    for n in range(N):
        if table[m][n] == 1 and visit[m][n] == 0:
            answer.append(area([m, n]))
print(len(answer))
answer = ' '.join(map(str, sorted(answer)))
print(answer)


