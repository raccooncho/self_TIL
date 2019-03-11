# def qsort(nums):
#     if len(nums) <= 1:
#         return nums
#     p = nums[len(nums) >> 1]
#     L = []
#     R = []
#     E = []
#     for n in nums:
#         if n < p:
#             L.append(n)
#         elif n > p:
#             R.append(n)
#         else:
#             E.append(n)
#     return qsort(L) + E + qsort(R)



# import heapq

# data = [69, 10, 30, 2, 16, 8, 31, 22]

# arr = []
# heapq.heapify(arr)

# for val in data:
#     heapq.heappush(arr, val)
#     print(arr)

# while arr:
#     val = heapq.heappop(arr)
#     print(val, end=" ")

# print()

# arr.clear()
# heapq.heapify(arr)

# for val in data:
#     heapq.heappush(arr, [-val, val])

# while arr:
#     p, val = heapq.heappop(arr)
#     print(val, end=" ")

# import sys
# sys.stdin = open('input.txt', 'r')

arr = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(A):
    if len(A) <= 1:  # 길이가 1이 되면 리턴한다.
        return A
    M = len(A) >> 1    # 위치상 중간을 기준으로
    L = merge_sort(A[M:])   # 반으로 쪼개서 왼쪽 오른쪽을 각각 다시 머지 소트 한다.
    R = merge_sort(A[:M])
    return merge(L, R)  # 각각 머지소트한 왼쪽 오른쪽 리스트를 머지로 합병한다.

def merge(l, r):
    result = []
    while len(l) > 0 and len(r) > 0:  # 둘중 하나의 리스트가 다 빌때까지
        if l[0] <= r[0]:  # 0번 인덱스가 작은 것을 result에 append시킨다.
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    if len(l) > 0:   # 남은 리스트를 result 에 합병시킨다.
        result += l
    else:
        result += r
    return result


arr = merge_sort(arr)
print(arr)




T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    answer = []
    for m in range(M):
        arr = list(map(int, input().split()))
        dum = []
        if len(answer) == 0:
            answer += arr
        else:
            for i in range(len(answer)):
                if answer[i] > arr[0]:
                    arr.append(answer[i])
                else:
                    dum.append(answer[i])
        if len(arr) >= 10:
            answer = arr
        else:
            answer = dum + arr
    result = []
    for i in range(1, 11):
        result.append(answer[-i])
    result = ' '.join(result)
    print('#{}{}'.format(t+1, result))















# T = int(input())
# for t in range(T):
#     N = int(input())
#     maps = []
#     for n in range(N):
#         row = list(map(int, input().split()))
#         maps += [row]
#     cnt = 0
#     def bus(n, d): # n은 현재 위치 [y, x], d는 버스의 방향 -> 0: 대각선, 1: 오른쪽, 2: 아래
#         global cnt  # cnt 로 도착하는 경우의 수를 세어준다.
#         if n == [N-1, N-1]: # 목적지에 도착하고
#             if d != 0: # 대각선 방향이 아니라면
#                 cnt += 1 # 카운트 + 1
#         else:
#             x = n[1]
#             y = n[0]
#             if x+1 < N and y < N and maps[y][x+1] == 0 and d != 2:
#                 bus([y, x+1], 1) # 오른쪽이 진행 가능하고 현재 진행 방향이 아래가 아니면 오른쪽으로 진행
#             if x < N and y + 1 < N and maps[y+1][x] == 0 and d != 1:
#                 bus([y+1, x], 2) # 아래가 진행 가능하고 현재 진행방향이 오른쪽이 아니면 아래로 진행
#             if x+1 < N and y+1 < N and maps[y][x+1] == 0 and maps[y+1][x] == 0 and maps[y+1][x+1] == 0:
#                 bus([y+1, x+1], 0) # 대각선이 진행 가능하면 대각선 진행
#     if maps[1][0] == 0: # 출발은 대각선 출발이 안되므로 [1, 0]과 [0,1]에서 출발
#         bus([1, 0], 2)
#     if maps[0][1] == 0:
#         bus([0, 1], 1)
#     print('#{} {}'.format(t+1, cnt))




# T = int(input())
# for t in range(T):
#     N = int(input())
#     light = list(map(int, input().split()))
#     answer = 0
#     for n in range(1, N+1):
#         if light[n-1] == 1:
#             i = 0
#             while i < N:
#                 if (i + 1) % n == 0:
#                     light[i] = abs(light[i] - 1)
#                 i += 1
#             answer += 1
#         if 1 not in light:
#             break
#     print('#{} {}'.format(t+1, answer))
































