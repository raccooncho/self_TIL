# 02_Search



### 1. 완전탐색 (Brute-force)

* 완전 탐색은 가능 한 모든 경우의 수를 찾는 방법이다.
* 가장 먼저, 순열을 찾아서 모든 순열에 원하는 조건을 대입하는 방법을 찾을 수 있다.

```python
arr = [1, 2, 3, 4]

for n in range(1 << len(arr)): # range == 0 ~ 2^len(arr)-1 == 0 ~ 15
    # 모든 경우의 수는 2^len(arr)개 이다.
    answer = []  # answer 에 각 경우의 수를 포함시킨다.
    for i in range(len(arr)): # 해당 수와 2^i승이 이진법에서 일치하는지 확인한다.
        if n & (1<<i):
            answer.append(arr[i]) # 일치하는 부분이 있으면 append한다.
    print(answer) # 해당 경우의 수를 출력한다. (다른 조건을 포함시킬 수도 있다. ex> 합계가 일정 값인 경우)
```



* 일정 수의 리스트에서 배치를 바꾸는 경우도 가능하다.

```python
arr = [1, 2, 3, 4]

def searching(arrr, n, answer):
    # arrr: 순열을 찾으려는 리스트
    # n : answer에 포함시킨 인덱스의 리스트
    # answer : arrr의 순열들이 포함되는 리스트
    if len(n) == len(arrr):
        print(answer) # arrr의 길이와 n에 해당하는 리스트의 길이가 같으면 print한다.
    else:
        for i in range(len(arrr)):
            if i not in n:
                m = n + [i] # n이 for문 돌면서 초기화가 되지 않으므로 m이라는 새로운 리스트에 i를 포함시켜서 재귀를 돌림
                answers = answer + [arrr[i]] # answer가 for문이 돌면서 초기화가 되지 않으므로 answers라는 새로운 리스트에 arrr[i]를 포함시켜서 재귀를 돌림
                searching(arrr, m, answers)
searching(arr, [], [])
```



* 패턴을 찾을 때도 완전탐색을 통해서 해결할 수 있다.

```python
string = 'amlskdmpozc;zlvm;ldkmzxlkcmvappleapsmd;zlvc'
finds = 'apple'
answer = []

for i in range(len(string) - len(finds) + 1): # 스트링에서 모든 경우의 수를 확인한다.
    n = 0 # 임시로 n이라는 값을 만들어서 값이 같을 때 마다 오른쪽으로 이동하면서 탐색한다.
    while n < len(finds): # n이 finds의 길이와 같아지면 멈춘다(탐색이 완료되어서 정답을 찾은 경우이므로)
        if string[i+n] == finds[n]: # 만약 값이 일치하면 n을 증가시킨다.
            n += 1
        else: # 값이 일치하지 않는다면 뒤는 볼 필요도 없이 틀리므로 while문을 탈출한다.
            break
    if n == len(finds): # n의 값이 finds의 길이와 같다면 원하는 문구를 찾은 것이므로 answer에 원하는 값을 추가시킨다.
        answer = [i, True]

if answer:
    print(answer)
else:
    print(False)
```



### 2. 이진검색 (binary search)

* 숫자나 알파벳 등이 정렬된 상태에서 원하는 값을 찾을때 사용하는 방법이다.
* 남은 값의 절반씩을 계속 제거하므로 매우 효율적이다.
* while 문을 활용하여 이진검색을 수행할 수 있다.

```python
arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 49, 62, 88]

def binarySearch(arr, key):
    start, end = 0, len(arr) - 1 # 맨 왼쪽과 맨 오른쪽 인덱스를 start, end로 설정함
    while start <= end: # start가 end보다 오른쪽에 위치할 때 까지 while문을 작동한다.
        mid = (start + end) >> 1  # 중간에 해당하는 index를 mid로 설정한다.
        if arr[mid] == key: # 탐색하는 값이 mid와 일치하면 mid를 return한다. 
            return mid
        elif arr[mid] > key: # 탐색하는 값보다 mid의 위치가 오른쪽에 존재한다면 
            end = mid - 1 # mid의 오른쪽을 모두 버린다. (end의 위치를 옮겨준다.)
        else:  # 탐색하는 값보다 mid의 위치가 왼쪽에 존재하면
            start = mid + 1 # mid의 왼쪽을 모두 버린다. (start의 위치를 옮겨준다.)
    return -1 # start와 end가 만날 때까지 mid값을 리턴하지 못했다면, 값을 찾지 못했다는 의미이므로 -1을 return 한다.
```



* 재귀함수를 활용하여 간단하게 탐색할 수 있다.

```python
arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 49, 62, 88]

def binary_search(arr, start, end, key):
    if start > end: # start가 end보다 오른쪽으로 넘어가면 값을 찾지 못한 것이므로 -1을 return한다.
        return -1
    mid = (start + end) >> 1 # start와 end의 중간 인덱스를 mid로 설정한다.
    if arr[mid] == key: # mid에 해당하는 값이 찾고자 하는 값과 일치하면 mid 값을 return 한다.
        return mid
    elif arr[mid] > key: # mid값이 찾고자 하는 값보다 오른쪽에 존재하면 mid의 오른쪽에 있는 값을 모두 버린다.
        return binary_search(arr, start, mid - 1, key) # end값을 mid로 재 설정 해준다.
    else: # mid값이 찾고자 하는 값보다 왼쪽에 존재하면 mid의 왼쪽에 존재하는 값을 모두 버린다.
        return binary_search(arr, mid + 1, end, key) # start를 mid로 재 설정 해준다.
```



### 3. KMP 알고리즘

**잠시포기**

```python
p = 'abcdabcef'                                                                       # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


m, n = len(p), len(t)
next = [0] * (m + 1) # 편의상 p의 길이보다 1 긴(인덱스 0을 버리기 위함..) 리스트를 생성

# 전처리
next[0] = -1 # 맨 앞을 시작의 의미로 -1로 설정
i, j = 0, -1
while i < m:
    while j >= 0 and p[j] != p[i]: # j 가 시작값인 -1이 되지 않기 위함..
        j = next[j]

    i, j = i + 1, j + 1
    next[i] = j

print(next)

# 매칭
i = j = 0
while i < n:
    while j >= 0 and p[j] != t[i]:
        j = next[j]

    i, j = i + 1, j + 1

    if j == m:
        print(i - j, t[:i - j], t[i - j:i - j + m], t[i - j + m:])
        break

```



### 4. DFS (Depth-First search)

* 깊이 우선탐색으로 한 방향으로 계속 탐색하다가 더이상 탐색을 진행할 수 없으면 돌아와서 다시 탐색하는 방법이다.

```python
def DFS(v):

    stack = []  # 빈 stack 을 생성
    stack.append(v)  # stack에 v를 추가
    visit[v] = True # visit 의 v를 True로 변경 (방문 표시)
    print(v, end=" ")

    while len(stack) > 0:
        prev = v # 시작위치 v를 저장해놓는다.
        for w in G[v]: # v에서 갈 수 있는 모든 경로 w
            if not visit[w]: # w가 만약 방문하지 않았다면
                stack.append(w) # stack에 w를 추가
                v = w # v를 w로 변경
                visit[w] = True # w의 방문위치를 기록
                print(v, end=" ")
                break # for문을 멈춤 -> w를 대상으로 다시 for문이 돈다
        if prev == v: # v가 변경되지 않았으면 더이상 갈 곳이 없단 의미이므로 stack에서 pop한다.
            v = stack.pop()
                        # stack가 모두 빌 때 까지 진행하면 방문 순서대로 print되는 것을 확인할 수 있다.
# ----------------------------------------------
import sys

sys.stdin = open("DFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)] 

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1) # 1부터 시작한다.
```

* 재귀로 해결할 수도 있다.

```python
def DFS(v):
    visit[v] = True

    print(v, end=" ")
    
    for w in G[v]:
        if not visit[w]:
            DFS(w)  # not visit일 때 마다 재귀로 계속 돌아간다 -> 모든게 visit이면 함수가 종료된다.
```

* DFS는 stack을 사용하여 뒤에서부터 제거하는 것이 낫다.



### 5. BFS (Breadth-First search)

* 너비 우선 탐색으로 동시에 진행 가능한 방향으로 탐색을 진행한다.

```python
from queue import Queue

def BFS(s, G):

    visit = [False] * (V + 1)
    D = [0] * (V + 1)

    Q = Queue()
    Q.put(s) # 큐에 s를 추가한다.
    visit[s] = True # s의 방문기록을 남긴다.
    print(s, end=" ")
    while not Q.empty(): # 큐가 빌때까지 진행한다.
        v = Q.get()
        for w in G[v]: # v에서 진행할수 있는 모든 방향 w에 대해서
            if not visit[w]: # 방문하지 않았다면
                D[w] = D[v] + 1 # 몇 번째 방문인지 기록한다.
                visit[w] = True # w의 방문기록을 남긴다.
                Q.put(w) # 큐에 w를 추가한다.
                print(w, end=" ")
    print()
    return D
# ----------------------------------------------

import sys
sys.stdin = open("BFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

D = BFS(1, G)
```

* BFS는 큐를 이용하여 앞에서 부터 제거해 나가는 것이 낫다.